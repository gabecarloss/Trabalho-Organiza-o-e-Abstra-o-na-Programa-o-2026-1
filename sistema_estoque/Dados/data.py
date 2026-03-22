import os
import csv
from sistema_estoque.Sistema.produto import Produto
from sistema_estoque.Sistema.cliente import Cliente

ARQ_CLIENTES = "clientes.csv"
ARQ_PRODUTOS = "produtos.csv"
ARQ_VENDAS = "vendas.csv"


def criar_arquivos():
    
    if not os.path.exists(ARQ_CLIENTES):
        open(ARQ_CLIENTES, "w").close()

    
    if not os.path.exists(ARQ_PRODUTOS):
        open(ARQ_PRODUTOS, "w").close()

    if not os.path.exists(ARQ_VENDAS):
        open(ARQ_VENDAS, "w").close()

def salvar_clientes(lista_clientes):
    with open(ARQ_CLIENTES, "w", newline="") as arquivo:
        writer = csv.writer(arquivo)
        atual = lista_clientes.cabeca
        while atual:
            c = atual.valor
            writer.writerow([c.id, c.nome, c.email])
            atual = atual.proximo


def salvar_produtos(lista_produtos):
    with open(ARQ_PRODUTOS, "w", newline="") as arquivo:
        writer = csv.writer(arquivo)
        atual = lista_produtos.cabeca
        while atual:
            p = atual.valor
            writer.writerow([p.id, p.nome, p.quantidade, p.preco])
            atual = atual.proximo


def salvar_vendas(lista_vendas):
    with open(ARQ_VENDAS, "w", newline="") as arquivo:
        writer = csv.writer(arquivo)
        atual = lista_vendas.cabeca
        while atual:
            v = atual.valor
            writer.writerow([v.id, v.cliente.id, v.produto.id, v.quantidade, v.valor_total])
            atual = atual.proximo


def carregar_clientes(lista_clientes):
    try:
        with open(ARQ_CLIENTES, "r") as arquivo:
            reader = csv.reader(arquivo)
            for linha in reader:
                if len(linha) >= 3:
                    cliente = Cliente(int(linha[0]), linha[1], linha[2])
                    lista_clientes.inserir(cliente)
    except FileNotFoundError:
        pass


def carregar_produtos(lista_produtos):
    try:
        with open(ARQ_PRODUTOS, "r") as arquivo:
            reader = csv.reader(arquivo)
            for linha in reader:
                if len(linha) >= 4:
                    produto = Produto(nome=linha[1], id_produto=int(linha[0]), quantidade=int(linha[2]), preco=float(linha[3]))
                    lista_produtos.inserir(produto)
    except FileNotFoundError:
        pass


def carregar_vendas(lista_vendas, lista_clientes, lista_produtos):
    try:
        with open(ARQ_VENDAS, "r") as arquivo:
            reader = csv.reader(arquivo)
            for linha in reader:
                if len(linha) >= 5:
                    cliente_id = int(linha[1])
                    produto_id = int(linha[2])
                    
                    cliente = buscar_cliente_por_id(lista_clientes, cliente_id)
                    produto = buscar_produto_por_id(lista_produtos, produto_id)
                    
                    if cliente and produto:
                        from sistema_estoque.Sistema.venda import Venda
                        venda = Venda(int(linha[0]), cliente, produto, int(linha[3]), float(linha[4]))
                        lista_vendas.inserir(venda)
    except FileNotFoundError:
        pass


def buscar_cliente_por_id(lista_clientes, cliente_id):
    atual = lista_clientes.cabeca
    while atual:
        if atual.valor.id == cliente_id:
            return atual.valor
        atual = atual.proximo
    return None


def buscar_produto_por_id(lista_produtos, produto_id):
    atual = lista_produtos.cabeca
    while atual:
        if atual.valor.id == produto_id:
            return atual.valor
        atual = atual.proximo
    return None
    for linha in reader:
            if len(linha) >= 4:
                linha.inserir (Produto( linha[0], linha[1], int(linha[2]), float(linha[3]))) 