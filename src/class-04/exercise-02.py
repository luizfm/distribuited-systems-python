class Node:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

class LoadBalancer:
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def distribute_task(self, task):
        # Simplified logic: send task to the node com menos tarefas
        target_node = min(self.nodes, key=lambda x: len(x.tasks))
        target_node.add_task(task)

# Exemplo de uso
if __name__ == "__main__":
    # Crie o balanceador de carga
    load_balancer = LoadBalancer()

    # Adicione alguns nodos
    node1 = Node()
    node2 = Node()
    node3 = Node()

    load_balancer.add_node(node1)
    load_balancer.add_node(node2)
    load_balancer.add_node(node3)

    # Crie algumas tarefas e distribua-as
    tasks = ["Task 1", "Task 2", "Task 3", "Task 4", "Task 5"]

    for task in tasks:
        load_balancer.distribute_task(task)

    # Verifique o estado dos nodos após a distribuição
    for i, node in enumerate(load_balancer.nodes):
        print(f"Node {i + 1} tasks: {node.tasks}")