import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)

while True:
    print("Waiting for a connection")
    connection, client_address = server_socket.accept()

    try:
    
      while True:
          data = connection.recv(1024)

          if(data):
             print("sending data to the client")
             print(data)
             connection.sendall(data)
          else:
             print("no more data")
             break
    finally:
       connection.close()
