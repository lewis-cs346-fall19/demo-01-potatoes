import socket
def main():
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	addr = ("localhost",17346)
	sock.connect(addr)
	for i in range (1,101):
		sock.sendall(str(i).encode())
		msg = sock.recv(1024).decode()
		print(str(i)+" -> "+msg)
	sock.close()
main()
