import socket

HOST = socket.gethostbyname(socket.gethostname())  # The server's hostname or IP address
PORT = 2050        # The port used by the server

# create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # bind the socket to a specific address and port
    s.bind((HOST, PORT))
    # listen for incoming connections
    s.listen(1)
    print('Server listening on', (HOST, PORT))
    # accept a new connection
    conn, addr = s.accept()
    print('Connected by', addr)
    with conn:
        while True:
            # receive data from the client
            data = conn.recv(1024)
            if not data:
                break
            # process the received data
            print('Received:', data.decode())
            # send a response back to the client
            #conn.sendall(b'OK')
            if data == "I have won!" or data == "I have lost!":
            	break
