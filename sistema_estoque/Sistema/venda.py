class Venda:

    def __init__(self, id_venda, cliente, produto, quantidade, valor_total):
        self.id = id_venda
        self.cliente = cliente
        self.produto = produto
        self.quantidade = quantidade
        self.valor_total = valor_total

    def __repr__(self):
        return f"Venda(id={self.id!r}, cliente={self.cliente!r}, produto={self.produto!r}, quantidade={self.quantidade}, valor_total={self.valor_total})"

    def processar_venda(self):
        if self.produto.quantidade >= self.quantidade:
            self.produto.atualizar_estoque(-self.quantidade)
            self.valor_total = self.quantidade * self.produto.preco
            return True
        else:
            return False

    def cancelar_venda(self):
        self.produto.atualizar_estoque(self.quantidade)
        self.valor_total = 0
        #.
        # Aqui você pode adicionar lógica para remover a venda da lista de vendas, se necessário.