import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(),25000))
s.listen()
conn, addr=s.accept()
conn.send("hey".encode())
sd=''
cd=''
print("let's chat")
while(sd!="bye" and cd!="bye"):
    cd=conn.recv(1024).decode()
    print("From client->",cd)
    sd=input("Server->")
    conn.send(sd.encode())  
conn.close()
socket.close()