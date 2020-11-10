import socket

for x in range(101):
    try:
        print('There is ' +socket.getservbyport(x, 'tcp') + ' service over TCP protocol in port number ' + str(x))
    except:
        print('There is no service in port ' + str(x))    

    