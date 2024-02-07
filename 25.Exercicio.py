#Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", 
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

def pergunta_vitima(mensagem):
    resposta = input(mensagem)
    return resposta

def contabilizar_resposta(resposta_1,resposta_2):
    contagem = 0
    if resposta_1 == "Sim":
        contagem =  contagem + 1 
        
    if resposta_2 == "Sim":
        contagem =  contagem + 1
    
    if resposta_3 == "Sim":
        contagem =  contagem + 1
    
    if resposta_4 == "Sim":
        contagem =  contagem + 1
    
    if resposta_5 == "Sim":
        contagem =  contagem + 1

    return contagem 

def gerar_classificacao(resultado_contagem):

    if resultado_contagem == 2:
        print ("Suspeito")
    elif resultado_contagem >=3 and resultado_contagem <=4:
        print ("Suspeito")
    elif resultado_contagem == 5:
        print ("Assassino")
    else:
        print ("Inocente")





resultado_resposta_1 = pergunta_vitima("Telefonou para a vítima? Sim ou Não ")
resultado_resposta_2 = pergunta_vitima("Esteve no local do crime? Sim ou Não ")
resposta_3 = pergunta_vitima("Mora perto da vítima? Sim ou Não ")
resposta_4 = pergunta_vitima("Devia para a vítima? Sim ou Não ")
resposta_5 = pergunta_vitima("Já trabalhou com a vítima? Sim ou Não ")
resultado_contar_respostas = contabilizar_resposta(resultado_resposta_1,resultado_resposta_2)
gerar_classificacao(resultado_contar_respostas)
 