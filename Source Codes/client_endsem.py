import socket
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((socket.gethostname(),12346))
string=input("Input string: ")
sock.sendto(string.encode(),(socket.gethostname(),12345))
data = sock.recvfrom(1024)
msg=data[0].decode()
if(msg=="true"):
    print("String is a palindrome")
else:
    print("String is not a palindrome")