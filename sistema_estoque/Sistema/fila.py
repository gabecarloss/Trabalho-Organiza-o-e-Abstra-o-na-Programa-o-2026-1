class fila:
    def __init__(self):
        self.fila = []

    def add (self, venda):
        self.fila.append(venda)

    def listar (self):
        if len(self.fila) == 0:
            print("Nenhuma venda registrada")
            return 
        elif len(self.fila) < 0:
            print("Erro: Fila com tamanho inválido")
            return
        
        for venda in self.fila:
            print(vars(venda))

    def enfileirar (self, venda):
        self.fila.append(venda)