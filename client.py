import socket
import classGround as cliCs

def click_join():
    # ip = socket.gethostbyname(socket.gethostname())
    # ip = "10.0.0.119"
    ip = input("Please input IP of the server: ")
    connect_port = 2029
    comms_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    comms_socket.connect((ip, connect_port))
    print("Connect to", ip)

    # arrange your ship
    enemyGroundClient = cliCs.EnemyGround()
    yourGroundClient = cliCs.YourGround()
    print("Let's play WarTanks!")

    connect_port1 = 2051
    comms_socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip3='192.168.227.136'
    comms_socket1.connect((ip3,  connect_port1))

    s = "Game has started!"
    comms_socket1.send(s.encode("UTF-8"))


    def client_send_dt(x):
        comms_socket.send(x.encode("UTF-8"))


    def layout():
        print("Enemy Ground:")
        enemyGroundClient.print_board(enemyGroundClient.grid_en)
        print("Your Ground:")
        yourGroundClient.print_board(yourGroundClient.grid_yo)
        # yourGroundClient.ships_info()


    layout()

    while True:
        # print("[Client] Connection Successful!!")
        # client input shoot point in server enemyGround
        # send_data = input("Input your target [row][column]: ")
        passY, passX = enemyGroundClient.target()
        send_data = str(passY) + str(passX)
        print(send_data)
        # client send point to server
        client_send_dt(send_data)
        # client get state flag from server to check if hit or not
        response = comms_socket.recv(64).decode("UTF-8")
        print(response)
        enemyGroundClient.flag = int(response)
        print(enemyGroundClient.flag)
        enemyGroundClient.change_cell(passX, passY, enemyGroundClient.flag) # changed
        # show game situation now
        layout()
        if enemyGroundClient.flag == 2:
            print("You Win")
            ip2= socket.gethostbyname(socket.gethostname())
            s= ip2 + " Wins the game"
            comms_socket1.send(s.encode("UTF-8"))
            comms_socket.close()
            break
        receive_pt = comms_socket.recv(64).decode("UTF-8")
        enemyGroundClient.flag = str(yourGroundClient.check_shoot(int(receive_pt[1]), int(receive_pt[0]))) # changed
        yourGroundClient.draw_cell(int(receive_pt[1]), int(receive_pt[0]), str(enemyGroundClient.flag))# changed
        layout()
        client_send_dt(enemyGroundClient.flag)
        if enemyGroundClient.flag == "2":
            print("You Loss")
            s = ip + " Wins the game"
            comms_socket1.send(s.encode("UTF-8"))
            comms_socket.close()
            break
