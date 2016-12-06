import socket

host = ''
port = 51423

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.setsocket(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

s.bind((host, port))
s.listen(5)