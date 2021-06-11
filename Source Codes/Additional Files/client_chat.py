import socket
c=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect((socket.gethostname(), 25000))
sd=''
cd=input("Client->")
c.send(cd.encode())
while(sd!="bye" and cd!="bye"):
    sd=c.recv(1024).decode()
    print("From server->",sd)
    cd=input("Client->")
    c.send(cd.encode())
c.close()