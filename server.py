import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the port on which you want to connect
port = 5000
SERVER= socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, port)

# Bind to the port
server_socket.bind(ADDR)

# Put the socket into listening mode
server_socket.listen(1)

print('Server is listening...')

# A forever loop until we interrupt it or an error occurs
while True:
   # Establish connection with client
   client_socket, addr = server_socket.accept()
   print('Got connection from', addr)

   # Send a 'thank you' message to the client
   message = 'Thank you for connecting'
   client_socket.send(message.encode())

   # Close the connection with the client
   client_socket.close()
