import socket
import classSea as serCs

def click_host():
    host_ip = socket.gethostbyname(socket.gethostname())
    port = 2029
    print("Host IP:", host_ip , "Port:", port)
    comms_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    comms_socket.bind((host_ip, port))
    comms_socket.listen(1)
    connection, address = comms_socket.accept()


    def server_send_dt(x):
        connection.send(x.encode("UTF-8"))


    # arrange your ship
    enemySea = serCs.EnemySea()
    yourSea = serCs.YourSea()

    print("Let's play Battleship!")


    def layout():
        print("Enemy sea:")
        enemySea.print_board(enemySea.grid_en)
        print("Your sea:")
        yourSea.print_board(yourSea.grid_yo)
        # yourSea.ships_info()


    layout()


    while True:
        # print("[Server] Connection Successful!!")
        # server receive points from client
        receive = connection.recv(64).decode("UTF-8")
        print(receive)
        # server checks if shoot or not in yourSea  must return some state
        enemySea.flag = str(yourSea.check_shoot(int(receive[1]), int(receive[0])))
        print(enemySea.flag)
        # server change the cell in yourSea
        yourSea.draw_cell(int(receive[1]), int(receive[0]), str(enemySea.flag))
        # show game situation now
        layout()
        # server send back state to client
        server_send_dt(enemySea.flag)
        if enemySea.flag == "2":
            print("You Loss")
            # disconnect add later
            comms_socket.close()
            break

        passY, passX = enemySea.target()
        print(passY, passX)
        send_data = str(passY) + str(passX)
        print(send_data)
        server_send_dt(send_data)

        rece_state = connection.recv(64).decode("UTF-8")
        print(rece_state)
        enemySea.flag = int(rece_state)
        enemySea.change_cell(passX, passY, enemySea.flag)
        layout()
        if enemySea.flag == 2:
            print("You Win")
            # disconnect add later
            comms_socket.close()
            break
