from socket import socket,AF_INET,SOCK_STREAM
'''
In [6]: gethostbyname("www.google.com")
Out[6]: '216.58.194.164'
'''

Socket = socket(AF_INET, SOCK_STREAM)
Socket.connect(('216.58.194.164',80))

Request  = b'GET / HTTP/1.1\r\n'
Request += b'Host: www.google.com\r\n'
Request += b'Connection: close\r\n'
Request += b'\r\n'
Socket.send(Request)

Response = b""

while True:
    Data = Socket.recv(1500)
    if not Data:
        break
    
    Response += Data
Socket.close()
print(Response)
