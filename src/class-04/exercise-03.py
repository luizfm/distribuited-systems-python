import random
import time

# Classe que representa um nó no sistema
class Node:
    def __init__(self, node_id):
        self.node_id = node_id  # ID único do nó
        self.is_alive = True    # Estado inicial: vivo

    def send_message(self, message):
        if self.is_alive:
            print(f"Node {self.node_id} sending message: {message}")  # Simula o envio de mensagem
            return "pong"
        else:
            raise Exception(f"Node {self.node_id} is not alive")

    def receive_message(self):
        if self.is_alive:
            return "ping"
        else:
            raise Exception(f"Node {self.node_id} is not alive")

    def check_health(self):
        # Simula a verificação de saúde do nó (pode retornar aleatoriamente True ou False)
        return random.choice([True, False])

# Classe que representa o sistema com vários nós
class System:
    def __init__(self, num_nodes):
        self.nodes = [Node(node_id) for node_id in range(num_nodes)]  # Cria uma lista de nós

    def get_active_node(self):
        for node in self.nodes:
            if node.is_alive:
                return node
        return None

    def perform_operation(self, message):
        active_node = self.get_active_node()
        if active_node:
            try:
                response = active_node.send_message(message)  # Tenta enviar a mensagem ao nó ativo
                print(f"Received response: {response}")
            except Exception as e:
                print(e)
                active_node.is_alive = False  # Marca o nó como falho se ocorrer uma exceção
                print(f"Node {active_node.node_id} is marked as failed.")
                self.perform_operation(message)  # Tenta novamente em outro nó ativo
        else:
            print("All nodes are down. System is unavailable.")

if __name__ == "__main__":
    num_nodes = 3
    system = System(num_nodes)

    while True:
        # Verifica a saúde de todos os nós
        for node in system.nodes:
            if not node.check_health():
                print(f"Node {node.node_id} has failed health check.")
                node.is_alive = False

        # Executa uma operação (envia "ping")
        system.perform_operation("ping")

        # Simula um atraso entre verificações de saúde e operações
        time.sleep(2)