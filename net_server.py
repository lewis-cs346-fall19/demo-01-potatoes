import socket
def main():
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	addr = ("0.0.0.0", 17346)
	sock.bind(addr)
	sock.listen(5)
	while True:
		(connectedSock, clientAddress) = sock.accept()
		while True:

			try:
				msg = connectedSock.recv(1024).decode()
				if msg!="":
					if int(msg)%2==0:
						returnMsg = int(msg)//2
					elif int(msg)==1:
						returnMsg = 1
					else:
						returnMsg = 3 *(int(msg)) + 1
					connectedSock.sendall(str(returnMsg).encode())
			except ConnectionAbortedError:
				sock.close()
				break
main()
