from sistema_estoque.Sistema.cliente import Cliente
from sistema_estoque.Sistema.produto import Produto
from sistema_estoque.Sistema.venda import Venda
from sistema_estoque.Sistema.lista_encadeada import Nolista
from sistema_estoque.Sistema.fila import fila
from sistema_estoque.Sistema.pilha import PilhaOperacoes as PilhaOp
from sistema_estoque.Dados.data import criar_arquivos

def main():
    criar_arquivos()
    clientes = Nolista()
    produtos = Nolista()
    vendas = Nolista()
    fila_atendimento = fila()
    pilha_operacoes = PilhaOp()

    while True:
        print("\n=== Sistema de Estoque ===")
        print("1. Cadastrar Cliente")
        print("2. Cadastrar Produto")
        print("3. Realizar Venda")
        print("4. Listar Clientes")
        print("5. Listar Produtos")
        print("6. Listar Vendas")
        print("7. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Nome do cliente: ")
            email = input("Email do cliente: ")
            cliente = Cliente(nome, email)
            clientes.inserir(cliente)
            pilha_operacoes.empilhar(f"Cliente cadastrado: {nome}")
            print("Cliente cadastrado com sucesso!")

        elif escolha == '2':
            nome = input("Nome do produto: ")
            try:
                preco = float(input("Preço do produto: "))
                produto = Produto(nome, preco)
                produtos.inserir(produto)
                pilha_operacoes.empilhar(f"Produto cadastrado: {nome}")
                print("Produto cadastrado com sucesso!")
            except ValueError:
                print("Erro: O preço deve ser um número.")

        elif escolha == '3':
            if clientes.cabeca is None or produtos.cabeca is None:
                print("Erro: Cadastre clientes e produtos antes de realizar uma venda.")
                continue
            nome_cliente = input("Nome do cliente para a venda: ")
            cliente_encontrado = None

            atual = clientes.cabeca
            while atual:
                if atual.valor.nome == nome_cliente:
                    cliente_encontrado = atual.valor
                    break
                atual = atual.proximo

            if not cliente_encontrado:
                print("Cliente não encontrado.")
                continue

            nome_produto = input("Nome do produto para a venda: ")
            produto_encontrado = None

            atual = produtos.cabeca
            while atual:
                if atual.valor.nome == nome_produto:
                    produto_encontrado = atual.valor
                    break
                atual = atual.proximo

            if not produto_encontrado:
                print("Produto não encontrado.")
                continue

            venda = Venda(cliente_encontrado, produto_encontrado)
            vendas.inserir(venda)
            fila_atendimento.enfileirar(venda)
            pilha_operacoes.empilhar(f"Venda: {cliente_encontrado.nome} comprou {produto_encontrado.nome}")
            print("Venda realizada com sucesso!")

        elif escolha == '7':
            print("Encerrando o sistema...")
            break

if __name__ == "__main__":
    main()