#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina
# ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#  Média de Aproveitamento  Conceito
#  Entre 9.0 e 10.0        A
#  Entre 7.5 e 9.0         B
#  Entre 6.0 e 7.5         C
#  Entre 4.0 e 6.0         D
#  Entre 4.0 e zero        E

def digita_nota(mensagem):
    nota = float(input(mensagem))
    return nota

def calcula_media(nota_1,nota_2):
    media = (nota_1+nota_2)/2
    return media

def verifica_conceito (media):

    if media >=9 and media<=10:
        conceito = "A"
        return conceito
    elif media >=7.5 and media<9.0:
        conceito = "B"
        return conceito
    elif media >=6.0 and media<7.5:
        conceito = "C"
        return conceito
    elif media >=4.0 and media<6.0:
        conceito = "D"
        return conceito
    elif media >4.0 :
        conceito = "E"
        return conceito

resultado_nota_1 = digita_nota("Digite a primeira nota: ")
resultado_nota_2 = digita_nota("Digite a segunda nota: ")
resultado_media = calcula_media(resultado_nota_1,resultado_nota_2)
resultado_conceito = verifica_conceito(resultado_media)
print("Com a média ",resultado_media, " O conceito para o aluno é: ",resultado_conceito )