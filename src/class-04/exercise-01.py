import socket
import threading
import time

class Node:
    def __init__(self, port):
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind(("localhost", port))
        self.alive = True

    def send_message(self, message, port):
        self.socket.sendto(message.encode(), ("localhost", port))

    def receive_message(self):
        data, addr = self.socket.recvfrom(1024)
        return data.decode()

    def detect_failure(self):
        while True:
            time.sleep(5)  # Intervalo de verificação de falhas
            try:
                self.socket.sendto(b"PING", ("localhost", self.port))
                self.socket.settimeout(2)  # Tempo de espera para resposta
                response, _ = self.socket.recvfrom(1024)
                if response.decode() != "PONG":
                    self.alive = False
                    print(f"Node {self.port} está inativo.")
                else:
                    self.alive = True
            except socket.timeout:
                self.alive = False
                print(f"Node {self.port} está inativo.")
            except Exception as e:
                print(f"Erro na detecção de falhas para o Node {self.port}: {e}")
                self.alive = False

    def run(self):
        threading.Thread(target=self.detect_failure, daemon=True).start()
        while True:
            message = input(f"Digite uma mensagem para enviar ao Node {self.port}: ")
            if self.alive:
                target_port = int(input("Digite a porta do nodo de destino: "))
                self.send_message(message, target_port)
            else:
                print(f"Node {self.port} está inativo. Não é possível enviar mensagens.")

if __name__ == "__main__":
    node1 = Node(5000)
    node2 = Node(5001)
    node3 = Node(5002)

    threading.Thread(target=node1.run).start()
    threading.Thread(target=node2.run).start()
    threading.Thread(target=node3.run).start()