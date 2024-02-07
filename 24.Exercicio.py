#Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
#O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
#par ou ímpar;
#positivo ou negativo;
#inteiro ou decimal.

def pergunta_numero(mensagem):
    numero = float(input(mensagem))

    return numero

def pergunta_opcao():
    opcao = int(input("Qual operação deseja realizar (digite o número correspondente):1 - soma, 2- multiplicação, 3- divisão, 4- subtração : "))

    return opcao

def selecionar_opcao(opcao,numero_1,numero_2):
    if opcao == 1: 
        resultado = numero_1 + numero_2
        return resultado
    elif opcao ==2:
        resultado = numero_1 * numero_2
        return resultado
    elif opcao ==3:
        resultado = numero_1 / numero_2
        return resultado
    elif opcao ==4:
        resultado = numero_1 - numero_2
        return resultado   
    
def verifica_par_impar(resultado):
    if resultado % 2 == 0:
        print("Número par")
    else:
        print("Número ímpar")

def verifica_positivo_negativo(resultado):

    if resultado > 0 :
        print("Número positivo")
    else:
        print("Número negativo")

def verifica_tipo_numero(resultado):

    if resultado == round(resultado):
        print("Número inteiro")

    else:
        print("Número real")

resultado_numero_1 = pergunta_numero("Digite o primeiro número: ")
resultado_numero_2 = pergunta_numero("Digite o segundo número: ")
resultado_pergunta_opcao = pergunta_opcao()
resultado_opcao = selecionar_opcao(resultado_pergunta_opcao,resultado_numero_1,resultado_numero_2)
print("Resultado",resultado_opcao)
verifica_par_impar(resultado_opcao)
verifica_positivo_negativo(resultado_opcao)
verifica_tipo_numero(resultado_opcao)