#Faça um Programa que peça os 3 lados de um triângulo.
#O programa deverá informar se os valores podem ser um triângulo. 
#Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
#Dicas:
#Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#Triângulo Equilátero: três lados iguais;
#Triângulo Isósceles: quaisquer dois lados iguais;
#Triângulo Escaleno: três lados diferentes;

def pergunta_lado(mensagem):
    lado = int(input(mensagem))
    return lado

def verifica_se_triangulo(lado_a,lado_b,lado_c):
#Esse verifica tá estranho
    if (lado_a<lado_b+lado_c) or (lado_b<lado_a+lado_c) or (lado_c<lado_a+lado_b):
        forma_triangulo(lado_a,lado_b,lado_c)
    else:
        print("Não é um triangulo")
    
def forma_triangulo(lado_a,lado_b,lado_c):
    if lado_a == lado_b ==lado_c:
        print("Triângulo Equilátero")
    elif lado_a == lado_b or lado_a == lado_c:
        print ("Triângulo isóscelos")
    elif lado_b == lado_a or lado_b == lado_c:  
        print ("Triângulo isóscelos")
    elif lado_c == lado_a or lado_c == lado_b:  
        print ("Triângulo isóscelos")
    elif lado_a != lado_b !=lado_c:
        print ("Triângulo escaleno")



primeiro_lado = pergunta_lado("Digite o primeiro lado :")
segundo_lado = pergunta_lado("Digite o segundo lado :")
terceiro_lado = pergunta_lado("Digite o terceiro lado :")

resultado_verifica = verifica_se_triangulo(primeiro_lado,segundo_lado,terceiro_lado)
