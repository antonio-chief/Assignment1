import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the port on which you want to connect
port = 5000
SERVER= socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, port)

# Connect to the server on local computer
client_socket.connect(ADDR)

# Send a 'thank you' message to the server
client_socket.send('Hello, Server!'.encode())

# Receive data from the server
data = client_socket.recv(1024)

print('Received', repr(data))

# Close the connection
client_socket.close()