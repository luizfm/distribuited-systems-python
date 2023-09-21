import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 12345))

def main():
      while True:
          message = input("Say something:")
          client_socket.send(message.encode())
          if message.lower() == 'sair':
             break
          response = client_socket.recv(1024).decode()
          print(f"A resposta foi: {response}")

      client_socket.close()


main()