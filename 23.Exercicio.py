#Faça um Programa que peça um número e informe se o número é inteiro ou decimal. 
#Dica: utilize uma função de arredondamento.

def digite_numero():
    numero = float(input("Digite o número e saiba se é inteiro ou decimal :"))
    return numero

def verifica_numero(numero):

    if numero == round(numero):
        print("Número inteiro")

    else:
        print("Número real")

resultado_numero = digite_numero()
print(resultado_numero)
verifica_numero(resultado_numero)