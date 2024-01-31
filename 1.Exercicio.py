#Faça um Programa que peça dois números e imprima o maior deles.

def pergunta_numero():
    numero = float(input("Digite um número:"))

    return numero

def verifica_numero(primeiro_numero,segundo_numero):

    if primeiro_numero > segundo_numero:
        return primeiro_numero
    elif segundo_numero > primeiro_numero:
        return segundo_numero

resposta_numero_1 = pergunta_numero()
resposta_numero_2 = pergunta_numero()
resultado_final  = verifica_numero(resposta_numero_1,resposta_numero_2)
print("O maior número é : ", resultado_final)