class PilhaOperacoes: 
    def __init__(self):
        self.pilha = []

    def empilhar (self, operacao):
        self.pilha.append(operacao)

    def retirar(self):
        if len(self.pilha) == 0:
            print("Nenhuma operação registrada")
            return None
        return self.pilha.pop()
     
    