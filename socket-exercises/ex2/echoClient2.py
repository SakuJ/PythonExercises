import socket
import threading

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print('connecting to %s port %s' % server_address)
sock.connect(server_address)

def send_message():
    while True:
        message = input(str("Write your message to server: "))
        message = message.encode('utf-8')
        if message:
            sock.sendall(message)
        else:
            print('Message is empty')


def receive_message():
    while True:
        rec_message = sock.recv(50)
        if len(rec_message) > 0:
            print('received "%s"' %rec_message)
            rec_message = ""

thread = threading.Thread(target=send_message)
thread2 = threading.Thread(target=receive_message)
thread.start()
thread2.start()