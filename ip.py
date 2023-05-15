import socket

hostname = socket.gethostname()
IP_address = socket.gethostbyname(hostname)
print(IP_address)
