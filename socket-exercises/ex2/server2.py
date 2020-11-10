import socket
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Bind socket to port
server_address = ('localhost', 10000)
print('starting up on %s port %s' %server_address)
sock.bind(server_address)

sock.listen(1)

def handle_client(connection, client_address):

    print('connection from', client_address)

    # Receive the data and retransmit it
    while True:
        data = connection.recv(50)
        if len(data) > 0:
            print('received "%s"' %data)
            data = ""

def send_message(connection, client_address):
    while True:
        message = input(str("Write your message: "))
        message = message.encode('utf-8')
        if message:
            connection.sendall(message)
        else:
            print('Message is empty')


#Waiting connection
print('waiting for a connection')
connection, client_address = sock.accept()
thread = threading.Thread(target=handle_client, args=(connection, client_address))
thread2 = threading.Thread(target=send_message, args=(connection, client_address))
thread.start()
thread2.start()



