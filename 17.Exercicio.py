#Faça um Programa que peça um número correspondente 
#a um determinado ano e em seguida informe se este ano é ou não bissexto.
import calendar
def informa_ano():
    ano = int(input("Digite o ano que deseja verificar:"))

    return ano

def verifica_bissexto(ano):
    
    if calendar.isleap(ano):
        print(f"{ano} é um ano bissexto.")
    else:
        print(f"{ano} não é um ano bissexto.")

resultado_ano = informa_ano()
verifica_bissexto(resultado_ano)

