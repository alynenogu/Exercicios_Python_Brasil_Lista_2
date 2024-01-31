#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

def pergunta_numero():
    numero = float(input("Digite o valor:"))
    return numero

def verifica_positivo_negativo(numero):

    if numero >0:
        resultado = "Positivo"
        return resultado
    elif numero <0:
        resultado = "Negativo"
        return resultado
    
resultado_numero = pergunta_numero()
resultado_verifica = verifica_positivo_negativo(resultado_numero)
print("O número digitado é : ", resultado_verifica)