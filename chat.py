# import socket
# import sys

# try:
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     print("socket successfully created")
# except socket.errors as err:
#     print("socket creTION FAILED WITH ERRORS %s" %(err))

# port = 90

# try:
#     local_ip = socket.gethostbyname("www.google.com")
# except socket.gaierror:

#     print("there was an error resolving the host")
#     sys.exit()

# s.connect((local_ip, port))
# print("the socket is successfully connected to google")