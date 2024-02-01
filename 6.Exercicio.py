#Faça um Programa que leia três números e mostre o maior deles.

def pergunta_numero(mensagem):
    numero = float(input(mensagem))

    return numero

def verifica_numero(primeiro_numero,segundo_numero,terceiro_numero):
    
    if primeiro_numero > segundo_numero and primeiro_numero > terceiro_numero:
        print("O primeiro número é maior",primeiro_numero)
    
    elif  segundo_numero > primeiro_numero and  segundo_numero > terceiro_numero:
        print("O segundo número é maior",segundo_numero)
    elif  terceiro_numero > primeiro_numero and  terceiro_numero > segundo_numero:
        print("O terceiro número é maior",terceiro_numero)
    else:
        print("Números iguais")

resultado_primeiro_numero = pergunta_numero("Digite o primeiro número: ")
resultado_segundo_numero = pergunta_numero("Digite o segundo número: ")
resultado_terceiro_numero = pergunta_numero("Digite o terceiro número: ")
verifica_numero(resultado_primeiro_numero,resultado_segundo_numero,resultado_terceiro_numero)