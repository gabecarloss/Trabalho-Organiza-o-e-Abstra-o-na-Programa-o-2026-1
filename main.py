from sistema_estoque.Sistema.cliente import Cliente
from sistema_estoque.Sistema.produto import Produto
from sistema_estoque.Sistema.venda import Venda
from sistema_estoque.Sistema.lista_encadeada import Nolista
from sistema_estoque.Sistema.fila import fila
from sistema_estoque.Sistema.pilha import PilhaOperacoes as PilhaOp
from sistema_estoque.Dados.data import criar_arquivos, carregar_clientes, carregar_produtos, carregar_vendas, salvar_clientes, salvar_produtos, salvar_vendas


def remover_por_nome(lista, nome):
    anterior = None
    atual = lista.cabeca
    while atual:
        if atual.valor.nome == nome:
            if anterior is None:
                lista.cabeca = atual.proximo
            else:
                anterior.proximo = atual.proximo
            return True
        anterior = atual
        atual = atual.proximo
    return False


def main():
    criar_arquivos()
    clientes = Nolista()
    produtos = Nolista()
    vendas = Nolista()
    fila_atendimento = fila()
    pilha_operacoes = PilhaOp()
    
    carregar_clientes(clientes)
    carregar_produtos(produtos)
    carregar_vendas(vendas, clientes, produtos)

    while True:
        print("\n=== Sistema de Estoque ===")
        print("1. Cadastrar Cliente")
        print("2. Cadastrar Produto")
        print("3. Realizar Venda")
        print("4. Listar Clientes")
        print("5. Listar Produtos")
        print("6. Listar Vendas")
        print("7. Remover Cliente")
        print("8. Remover Produto")
        print("9. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Nome do cliente: ")
            email = input("Email do cliente: ")
            proximo_id = 1
            atual = clientes.cabeca
            while atual:
                if atual.valor.id >= proximo_id:
                    proximo_id = atual.valor.id + 1
                atual = atual.proximo
            cliente = Cliente(id_cliente=proximo_id, nome=nome, email=email)
            clientes.inserir(cliente)
            salvar_clientes(clientes)
            pilha_operacoes.empilhar(f"Cliente cadastrado: {nome}")
            print("Cliente cadastrado com sucesso!")

        elif escolha == '2':
            nome = input("Nome do produto: ")
            try:
                preco = float(input("Preço do produto: "))
                quantidade = int(input("Quantidade em estoque: "))
                proximo_id = 1
                atual = produtos.cabeca
                while atual:
                    if atual.valor.id_produto >= proximo_id:
                        proximo_id = atual.valor.id_produto + 1
                    atual = atual.proximo
                produto = Produto(nome=nome, id_produto=proximo_id, quantidade=quantidade, preco=preco)
                produtos.inserir(produto)
                salvar_produtos(produtos)
                pilha_operacoes.empilhar(f"Produto cadastrado: {nome}")
                print("Produto cadastrado com sucesso!")
            except ValueError:
                print("Erro: O preço e quantidade devem ser números.")

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

            try:
                quantidade_venda = int(input("Quantidade a vender: "))
                
                if quantidade_venda > produto_encontrado.quantidade:
                    print(f"Erro: Apenas {produto_encontrado.quantidade} unidades disponíveis em estoque.")
                    continue
                
                valor_total = quantidade_venda * produto_encontrado.preco
                produto_encontrado.quantidade -= quantidade_venda
                
                proximo_id_venda = 1
                atual_venda = vendas.cabeca
                while atual_venda:
                    if atual_venda.valor.id_venda >= proximo_id_venda:
                        proximo_id_venda = atual_venda.valor.id_venda + 1
                    atual_venda = atual_venda.proximo
                
                venda = Venda(id_venda=proximo_id_venda, cliente=cliente_encontrado, produto=produto_encontrado, quantidade=quantidade_venda, valor_total=valor_total)
                vendas.inserir(venda)
                fila_atendimento.enfileirar(venda)
                salvar_vendas(vendas)
                salvar_produtos(produtos)
                pilha_operacoes.empilhar(f"Venda: {cliente_encontrado.nome} comprou {produto_encontrado.nome}")
                print(f"Venda realizada com sucesso!")
                print(f"Quantidade: {quantidade_venda} unidade(s)")
                print(f"Valor Total: R$ {valor_total:.2f}")
            except ValueError:
                print("Erro: A quantidade deve ser um número.")

        elif escolha == '4':
            print("\n=== Clientes Cadastrados ===")
            if clientes.cabeca is None:
                print("Nenhum cliente cadastrado.")
            else:
                atual = clientes.cabeca
                while atual:
                    print(f"Nome: {atual.valor.nome} | Email: {atual.valor.email}")
                    atual = atual.proximo

        elif escolha == '5':
            print("\n=== Produtos Cadastrados ===")
            if produtos.cabeca is None:
                print("Nenhum produto cadastrado.")
            else:
                atual = produtos.cabeca
                while atual:
                    print(f"Nome: {atual.valor.nome} | Preço: R$ {atual.valor.preco:.2f} | Quantidade: {atual.valor.quantidade}")
                    atual = atual.proximo

        elif escolha == '6':
            print("\n=== Vendas Realizadas ===")
            if vendas.cabeca is None:
                print("Nenhuma venda realizada.")
            else:
                atual = vendas.cabeca
                while atual:
                    print(f"Cliente: {atual.valor.cliente.nome} | Produto: {atual.valor.produto.nome} | Valor Total: R$ {atual.valor.valor_total:.2f}")
                    atual = atual.proximo

        elif escolha == '7':
            nome_remover = input("Nome do cliente a remover: ")
            if remover_por_nome(clientes, nome_remover):
                salvar_clientes(clientes)
                print("Cliente removido com sucesso.")
            else:
                print("Cliente não encontrado.")

        elif escolha == '8':
            nome_remover = input("Nome do produto a remover: ")
            if remover_por_nome(produtos, nome_remover):
                salvar_produtos(produtos)
                print("Produto removido com sucesso.")
            else:
                print("Produto não encontrado.")

        elif escolha == '9':
            print("Encerrando o sistema...")
            break

if __name__ == "__main__":
    main()