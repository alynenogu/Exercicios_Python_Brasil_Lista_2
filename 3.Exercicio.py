#Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
#Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

def pergunta_letra():
    pergunta = input("Digite um sexo -> F- Feminino ou M- Masculino: ")
    return pergunta

def verifica_letra(pergunta):

    if pergunta == "F":
        print("Feminino")
    elif pergunta == "M":
        print("Masculino")
    else:
        print("Sexo inválido")

resposta = pergunta_letra()
verifica_letra(resposta)