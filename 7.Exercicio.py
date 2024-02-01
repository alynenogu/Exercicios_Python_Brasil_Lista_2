#Faça um Programa que leia três números e mostre o maior e o menor deles.

def pergunta_numero(mensagem):
    numero = float(input(mensagem))

    return numero

def verifica_maior_numero(primeiro_numero,segundo_numero,terceiro_numero):

    if primeiro_numero > segundo_numero and primeiro_numero > terceiro_numero:
        print("O primeiro número é maior ",primeiro_numero)
    elif  segundo_numero > primeiro_numero  and  segundo_numero > terceiro_numero :
        print("O segundo número é maior ",segundo_numero)
    elif  terceiro_numero > primeiro_numero  and  terceiro_numero > segundo_numero :
        print("O terceiro número é maior ",terceiro_numero)
    else:
        print("Números iguais")

def verifica_menor_numero(primeiro_numero,segundo_numero,terceiro_numero):

    if primeiro_numero < segundo_numero and primeiro_numero < terceiro_numero:
        print("O primeiro número é menor ",primeiro_numero)
    elif  segundo_numero < primeiro_numero  and  segundo_numero < terceiro_numero :
        print("O segundo número é menor ",segundo_numero)
    elif  terceiro_numero < primeiro_numero  and  terceiro_numero < segundo_numero :
        print("O terceiro número é menor ",terceiro_numero)
    else:
        print("Números iguais")

resultado_primeiro_numero = pergunta_numero("Digite o primeiro número: ")
resultado_segundo_numero = pergunta_numero("Digite o segundo número: ")
resultado_terceiro_numero = pergunta_numero("Digite o terceiro número: ")
verifica_maior_numero(resultado_primeiro_numero,resultado_segundo_numero,resultado_terceiro_numero)
verifica_menor_numero(resultado_primeiro_numero,resultado_segundo_numero,resultado_terceiro_numero)