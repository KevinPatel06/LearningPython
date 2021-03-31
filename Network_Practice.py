import socket
import requests, json, time

# mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# AF.INET creates the socket and sock_stream has characters come one after another
# mySocket.connect(('data.pr4e.org', 80))
# print(mySocket.getsockname())

api = "https://blockchain.info/ticker"
apinew = "https://blockchain.info/tobtc?currency=USD&value=500"
response = requests.get(api)
set = []
print(response.json())
