#Faça um Programa para leitura de três notas parciais de um aluno.
#O programa deve calcular a média alcançada por aluno e presentar:
#A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
#A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
#A mensagem "Aprovado com Distinção", se a média for igual a 10.

def pergunta_notas(mensagem):
    nota = float(input(mensagem))

    return nota

def calcula_media(nota_1,nota_2,nota_3):
    media = (nota_1+nota_2+nota_3)/3

    return media
def verifica_media (media):

    if media >= 7 and media <10:
        print ("Aprovado com média",media)
    elif media == 10:
        print ("Aprovado com Distinção ",media)
    elif media < 7:
        print ("Reprovado com média",media)

resultado_nota_1 = pergunta_notas("Digite a primeira nota :")
resultado_nota_2 = pergunta_notas("Digite a segunda nota :")
resultado_nota_3 = pergunta_notas("Digite a terceira nota :")
resultado_media = calcula_media(resultado_nota_1,resultado_nota_2,resultado_nota_3)
verifica_media(resultado_media)