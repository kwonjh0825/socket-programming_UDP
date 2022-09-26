from socket import *

serverName = '127.0.0.1'

serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)
# clientSocket.connect((serverName, serverPort))

while True:
    sentence = input('input (q to quit) : ')
    if sentence == "q" or sentence == "Q":
        break
    clientSocket.sendto(sentence.encode(), (serverName, serverPort))

    result, serverAddr = clientSocket.recvfrom(2048)
    print("result : ", result.decode())

clientSocket.close()