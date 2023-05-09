import socket

hostname = socket.gethostname()
IP_address = socket.gethostbyname(hostname)
print("192.168.192.210:", IP_address)
