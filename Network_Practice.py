import socket

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# AF.INET creates the socket and sock_stream has characters come one after another
mySocket.connect(('data.pr4e.org', 80))
print(mySocket.getsockname())