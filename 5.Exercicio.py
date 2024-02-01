#Faça um programa para a leitura de duas notas parciais de um aluno. 
#O programa deve calcular a média alcançada por aluno e apresentar:
#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#A mensagem "Reprovado", se a média for menor do que sete;
#A mensagem "Aprovado com Distinção", se a média for igual a dez.

def digite_nota(mensagem):
    nota = float(input(mensagem))

    return nota

def calcula_media(nota1, nota2):
    media = (nota1 + nota2)/2

    return media

def verifica_media(media):
    if media >=7 and media <9 :
        print("Aprovado")
    elif media < 7:
        print("Reprovado")
    elif media == 10:
        print("Aprovado com Distinção")

resposta_nota_1 = digite_nota("Digite a primeira nota : ")
resposta_nota_2 = digite_nota("Digite a segunda nota : ")
resposta_media = calcula_media(resposta_nota_1,resposta_nota_2)
verifica_media(resposta_media)