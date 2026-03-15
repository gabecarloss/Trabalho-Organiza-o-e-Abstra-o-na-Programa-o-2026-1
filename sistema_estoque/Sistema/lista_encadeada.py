class Nolista:

    def __init__(self, valor):
        self.valor = valor 
        self.proximo = None 
        
        


    class ListaEncadeada:

        def __init__(self):
            self.head = None 

        def adicionar(self, valor):
            novo = Nolista(valor)
            if self.head is None:   #verifica tem tem algum dado na lista rpz, none = lista vazia
                self.head = novo 
            else:                   #caso tenha algum elementooo  head → [A] → [B] → [C] → None
                atual = self.head                                      #atual
                while atual.proximo: #vai até o ultimo dado da lista
                    atual = atual.proximo 
                atual.proximo = novo


        def listar (self):
            atual = self.head 
            if atual is None:
                print("Lista vazia")
            else:
                while atual: 
                    print(vars(atual.valor))      #vars retorna as váriaveis do dentro de um objeto ou várivel, váriavel não tenho ctz ainda mas objeto sim.
                    atual = atual.proximo2


        def buscar_id (self, id):
            atual = self.head 
            while atual:
                if atual.valor.id == id:
                    return atual.valor 
                atual = atual.proximo
            