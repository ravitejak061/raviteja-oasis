import socket

# create a socket
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connecting to server 
s_addr = ("localhost",9999)
c.connect(s_addr)

# sending data to server
data = "hii server!"
c.send(data.encode())

# recieve reply from server
reply = c.recv(1024)
print("Messsage from server:", reply.decode())

# closing
c.close()

