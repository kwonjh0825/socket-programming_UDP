from socket import *

serverName = '127.0.0.1'
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(('', serverPort))

sumSocket = socket(AF_INET, SOCK_DGRAM)
mulSocket = socket(AF_INET, SOCK_DGRAM)

result = ''
r = ''

while True:
    s, clientAddr = serverSocket.recvfrom(2048)
    string = s.decode()
    if string == 'q':
        break
    else:
        if '+' in string or '-' in string:              # send to plus_minus_server
            sumSocket.sendto(string.encode(), (serverName, 9998))

            r, sumserverAddr = sumSocket.recvfrom(2048)
            result = r.decode()
        elif '*' in string or '/' in string:            # send to times_div_server
            mulSocket.sendto(string.encode(), (serverName, 9999))

            r, mulserverAddr = mulSocket.recvfrom(2048)
            result = r.decode()
        serverSocket.sendto(result.encode(), clientAddr) 
