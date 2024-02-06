#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
from datetime import datetime

def pergunta_data():
    data = input("Informe a data: ")
    return data

def verifica_dados(data):


#Funciona com Data válida (por exemplo, 05/01/24). Mas não funciona com data inválida. Como corrigir?
    if datetime.strptime(data, "%d/%m/%y"):
        print("Data válida")
    else:
        print("Data inválida")

resposta_data = pergunta_data()
verifica_dados(resposta_data)



