import hashlib

# Classe para representar um nó com informações como ID e chave secreta
class Node:
    def __init__(self, node_id, secret_key):
        self.node_id = node_id
        self.secret_key = secret_key
        # Calcula o hash da chave secreta e armazena-o como key_hash
        self.key_hash = hashlib.sha256(secret_key.encode()).hexdigest()

# Função para autenticar um nó com base em sua chave secreta
def authenticate(node, secret_key):
    # Calcula o hash da chave secreta fornecida
    hash_key = hashlib.sha256(secret_key.encode()).hexdigest()
    # Compara o hash da chave fornecida com o hash armazenado no nó
    if node.key_hash == hash_key:
        return True
    return False

# Exemplo de uso:
node1 = Node("node1", "senha1")
node2 = Node("node2", "senha2")

# Autenticar um nó
authenticated = authenticate(node1, "senha1")
if authenticated:
    print("Nó autenticado com sucesso.")
else:
    print("Falha na autenticação.")