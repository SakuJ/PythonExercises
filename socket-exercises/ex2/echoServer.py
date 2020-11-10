import socket
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Bind socket to port
server_address = ('localhost', 10000)
print('starting up on %s port %s' %server_address)
sock.bind(server_address)

sock.listen(1)

def handle_client(connection, client_address):
    try:
        print('connection from', client_address)

        # Receive the data and retransmit it
        while True:
            data = connection.recv(50)
            print('received "%s"' %data)
            if data:
                print('sending data back to the client')
                connection.sendall(data)
            else:
                print('no more data from', client_address)
                break
            
    finally:
        # Clean up the connection
        connection.close()

while True:
    #Waiting connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    thread = threading.Thread(target=handle_client, args=(connection, client_address))
    thread.start()
    print(f"[ACTIVE CONNECTIONS] {threading.activeCount() -1}")


