#Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas,
#dezenas e unidades do mesmo.
#Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
#326 = 3 centenas, 2 dezenas e 6 unidades
#12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 
#311, 111, 25, 20, 10, 21, 11, 1, 7 e 1

def pergunta_numero():
    numero = float(input("Informe um número menor que 1000 :"))

    return numero

def calcula_quantidade(numero):
    
    
    if numero < 1000: 
        centenas = numero // 100
        resto = numero % 100
        dezenas = resto // 10
        unidades = resto % 10

        print("Centenas: ", centenas, "dezenas: ", dezenas, "unidades :", unidades)
    else:
        print("Maior que 1000")

resultado_numero = pergunta_numero()
calcula_quantidade(resultado_numero)

