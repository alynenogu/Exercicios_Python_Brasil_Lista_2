#Faça um Programa para um caixa eletrônico.
#O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão 
#fornecidas. 
#As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. 
#O valor mínimo é de 10 reais e o máximo de 600 reais. 
#O programa não deve se preocupar com a quantidade de notas existentes na máquina.
#Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100,
#uma nota de 50, uma nota de 5 e uma nota de 1;
#Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, 
#ma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

def informa_saque ():
    valor_saque = float(input("Qual é o valor do saque? "))

    return  valor_saque

def qtd_notas(valor_saque):

    if valor_saque < 10 or valor_saque > 600:
        print("O valor mínimo é de 10 reais e o máximo de 600.")
    else:
        notas_100 = valor_saque//100
        resto_100 = valor_saque%100
        notas_50 = resto_100//50
        resto_50 = resto_100%50
        notas_10 = resto_50//10
        resto_10 = resto_50%10
        notas_5 = resto_10//5
        notas_1 = resto_10%5

        return notas_100,notas_50, notas_10, notas_5,notas_1


resultado_valor_reais = informa_saque()
resultado_qtd_notas_100,resultado_qtd_notas_50,resultado_qtd_notas_10,resultado_qtd_notas_5,resultado_qtd_notas_1  = qtd_notas(resultado_valor_reais)

print("Necessário R$100 -  Qtd", resultado_qtd_notas_100,"R$50 - Qtd", resultado_qtd_notas_50, "R$10 - Qtd", resultado_qtd_notas_10,"R$5 - Qtd", resultado_qtd_notas_5,"R$1 - Qtd",resultado_qtd_notas_1)