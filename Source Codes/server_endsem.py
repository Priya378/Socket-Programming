import socket
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((socket.gethostname(),12345))
print("Waiting for client to send string")
data = sock.recvfrom(1024)
print("Received String is:",data[0].decode())
string=data[0].decode()
reverse=string[::-1]
if(string==reverse):
    msg="true"
else:
    msg="false"
sock.sendto(msg.encode(),(socket.gethostname(),12346))
print("End of the program")