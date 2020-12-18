import socket

ip = input("Enter your ip: ")
p = int(input("Enter port: "))

c = socket.gethostname()

print("Server Started...waiting client to connect")

def Connection():
    s = socket.socket()
    s.bind((ip,p))
    s.listen(1)
    con, addr = s.accept()
    print("Type ' bye ' to close session")
    print(f"Client hostname is => {c}")
    print(addr, " Client Is Connected")
    
    while True:
          rev = input("Shell~: ")
          if(rev =="bye"):
              con.send('bye'.encode())
              con.close()
              break
          else:
            con.send(rev.encode())
            print(con.recv(1024).decode())
      
Connection()      
