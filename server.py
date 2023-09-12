import socket
import classGround as serCs

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
    enemyGround = serCs.EnemyGround()
    yourGround = serCs.YourGround()

    print("Let's play Battleship!")


    def layout():
        print("Enemy Ground:")
        enemyGround.print_board(enemyGround.grid_en)
        print("Your Ground:")
        yourGround.print_board(yourGround.grid_yo)
        # yourGround.ships_info()


    layout()


    while True:
        # print("[Server] Connection Successful!!")
        # server receive points from client
        receive = connection.recv(64).decode("UTF-8")
        print(receive)
        # server checks if shoot or not in yourGround  must return some state
        enemyGround.flag = str(yourGround.check_shoot(int(receive[1]), int(receive[0])))
        print(enemyGround.flag)
        # server change the cell in yourGround
        yourGround.draw_cell(int(receive[1]), int(receive[0]), str(enemyGround.flag))
        # show game situation now
        layout()
        # server send back state to client
        server_send_dt(enemyGround.flag)
        if enemyGround.flag == "2":
            print("You Loss")
            # disconnect add later
            comms_socket.close()
            break

        passY, passX = enemyGround.target()
        print(passY, passX)
        send_data = str(passY) + str(passX)
        print(send_data)
        server_send_dt(send_data)

        rece_state = connection.recv(64).decode("UTF-8")
        print(rece_state)
        enemyGround.flag = int(rece_state)
        enemyGround.change_cell(passX, passY, enemyGround.flag)
        layout()
        if enemyGround.flag == 2:
            print("You Win")
            # disconnect add later
            comms_socket.close()
            break
