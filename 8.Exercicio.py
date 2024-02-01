#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
#sabendo que a decisão é sempre pelo mais barato.

def pergunta_nome_produto(mensagem):
    nome_produto = input(mensagem)
    return nome_produto

def pergunta_preco(mensagem):
    preco = float(input(mensagem))
    return preco

def verificar_menor_preco (resposta_nome_produto,primeiro_preco,segundo_preco,terceiro_preco):

    if primeiro_preco < segundo_preco and primeiro_preco < terceiro_preco:
        print("Para o produto ", resposta_nome_produto, "O primeiro produto é mais barato",primeiro_preco)
    elif segundo_preco < primeiro_preco and segundo_preco < terceiro_preco:
        print("Para o produto ", resposta_nome_produto, "O segundo produto é mais barato",segundo_preco)
    elif terceiro_preco < primeiro_preco and terceiro_preco < primeiro_preco:
        print("Para o produto ", resposta_nome_produto, "O terceiro produto é mais barato",terceiro_preco)

nome_produto = pergunta_nome_produto("Qual o nome do produto? ")
resultado_preco_1 = pergunta_preco("Qual é o primeiro preço encontrado : R$")
resultado_preco_2 = pergunta_preco("Qual é o segundo preço encontrado : R$")
resultado_preco_3 = pergunta_preco("Qual é o terceiro preço encontrado : R$")
verificar_menor_preco(nome_produto,resultado_preco_1,resultado_preco_2,resultado_preco_3)