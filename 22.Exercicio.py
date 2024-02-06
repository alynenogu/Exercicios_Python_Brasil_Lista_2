#Faça um Programa que peça um número inteiro e 
#determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).
def pergunta_numero ():
    numero = int(input("Digite um número?"))

    return numero

def verifica_par_impar(numero):

    if numero%2 == 0:
        print("Esse número é par! ")
    else:
        print("Esse número é ímpar! ")

resposta_numero = pergunta_numero()
verifica_par_impar(resposta_numero)