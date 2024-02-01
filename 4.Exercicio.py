#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

def pergunta_letra():
    pergunta = input("Digite uma letra : ")
    return pergunta

def verifica_letra(letra):

    if letra =="A" or letra == "E" or letra=="I" or letra=="O" or letra=="U":
        print("Vogal")
    else:
        print("Consoante")

resposta_pergunta = pergunta_letra()
verifica_letra(resposta_pergunta)
 


