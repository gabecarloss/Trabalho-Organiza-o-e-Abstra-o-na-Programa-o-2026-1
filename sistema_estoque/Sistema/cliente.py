class Cliente:

    def __init__(self, id_cliente, nome, email):
        self.id = id_cliente
        self.nome = nome
        self.email = email

    def __repr__(self):
        return f"Cliente(id={self.id!r}, nome={self.nome!r}, email={self.email!r})"

    def cadastrar_cliente(self, lista_clientes):
        lista_clientes.inserir(self)

    def listar_clientes(self, lista_clientes):
        clientes = []
        atual = lista_clientes.head
        while atual:
            clientes.append(atual.valor)
            atual = atual.proximo
        return clientes