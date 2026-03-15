import os
import csv
from sistema_estoque.Sistema.produto import Produto

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
    with open (ARQ_CLIENTES, "w", newline= "") as arquivo:
        writer = csv.writer(arquivo)

        atual = lista_clientes.head
        while atual:
            c = atual.valor
            writer.writerow([c.id, c.nome]) #vai retornar o id e nome do cliente
            atual = atual.proximo

def salvar_produtos(lista_produtos):
    with open (ARQ_PRODUTOS, "w", newline= "") as arquivo:
        writer = csv.writer(arquivo)

        atual = lista_produtos.head
        while atual:
            p = atual.valor
            writer.writerow([p.id, p.nome, p.quantidade, p.preco])      #vai retornar o id, nome, quantidade e preço do produto
            atual = atual.proximo

def salvar_vendas(lista_vendas):
    with open (ARQ_VENDAS, "w", newline= "") as arquivo:
        writer = csv.writer(arquivo)

        atual = lista_vendas.head
        while atual:
            v = atual.valor
            writer.writerow([v.id, v.cliente.id, v.produto.id, v.quantidade, v.valor_total])      #vai retornar o id da venda, id do cliente, id do produto, quantidade e valor total da venda
            atual = atual.proximo


def carregar_clientes(lista_clientes):
    with open  (ARQ_CLIENTES, "r") as arquivo:
        reader = csv.reader(arquivo)
        for linha in reader:
            if len(linha) >= 4:
                linha.inserir (Produto( linha[0], linha[1], int(linha[2]), float(linha[3]) ) ) #vai ler o id, nome, quantidade e preço do produto e inserir na lista de produtos

       