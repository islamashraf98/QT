
import socket               # Import socket module
s = socket.socket()         # Create a socket object
host = '127.0.0.1' # Get local machine name
port = 8000                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   data = c.recv(1024)
   print ('Got connection from', addr)
   print (data)
   c.close()                # Close the connection