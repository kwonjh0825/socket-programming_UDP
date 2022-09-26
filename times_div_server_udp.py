from socket import *

serverName = '127.0.0.1'
serverPort = 9999
serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind((serverName, serverPort))

result = 0
r = 0
oper = ''


while True:
	s, midserverAddr = serverSocket.recvfrom(2048)
	string = s.decode()

	for i in string:	
		if i == '*' or i == '/':
			oper = i
			idx = string.index(i)

	if oper == '*':
		r = int(string[0:idx]) * int(string[idx+1:])
	elif oper == '/':
		r = int(string[0:idx]) / int(string[idx+1:])

	print(f"{string} = {r}")
        
	result = str(r)
        
	serverSocket.sendto(result.encode(), midserverAddr)