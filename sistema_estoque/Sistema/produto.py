class Produto:
    def __init__(self, id_produto, nome, quantidade, preco):
        self.id = int(id_produto)
        self.nome = nome
        self.quantidade = int(quantidade)
        self.preco = float(preco)