import socket
hostname=socket.gethostname()
IPAddr=socket.gethostbyname(hostname)
print(hostname)
print("My ip adress is:",IPAddr)