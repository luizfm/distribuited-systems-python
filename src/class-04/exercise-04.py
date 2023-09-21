import threading

# Simulando uma lista compartilhada entre os nós
shared_data = []
# Nós da rede
all_nodes = []

# Classe para representar um nó
class Node:
    def __init__(self, node_id):
        self.node_id = node_id

    def send_message(self, message):
        for other_node in all_nodes:
            if other_node != self:
                other_node.receive_message(self.node_id, message)

    def receive_message(self, sender_id, message):
        # Processa a mensagem recebida e atualiza os dados compartilhados
        if message.startswith("update:"):
            data = message[len("update:"):]
            self.update_data(data)
            print(f"Node {self.node_id} recebeu uma atualização de {sender_id}: {data}")

    def update_data(self, data):
        # Atualiza os dados compartilhados com exclusão mútua
        with data_lock:
            shared_data.append(data)

# Inicialização dos nós e do lock para exclusão mútua
data_lock = threading.Lock()
for i in range(3):  # Número de nós na rede (exemplo: 3 nós)
    node = Node(i)
    all_nodes.append(node)

# Exemplo de atualização de dados em um nó
def update_data(node, data):
    node.update_data(data)
    node.send_message(f"update:{data}")

# Testando o protocolo
update_data(all_nodes[0], "Novos dados 1")
update_data(all_nodes[1], "Novos dados 2")
update_data(all_nodes[2], "Novos dados 3")