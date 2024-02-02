#Faça um Programa que leia um número e exiba o dia correspondente da semana.
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

def digite_numero_dia_semana():
    numero_dia_semana = int(input("Digite o número para o dia da semana, sendo 1-Domingo, 2- Segunda etc :"))
    return numero_dia_semana

def exibe_dia(numero_dia_semana):
    if numero_dia_semana==1:
        nome_semana = "Domingo"
        return nome_semana
    elif numero_dia_semana ==2:
        nome_semana="Segunda"
        return nome_semana
    elif numero_dia_semana ==3:
        nome_semana="Terça"
        return nome_semana
    elif numero_dia_semana ==4:
        nome_semana="Quarta"
        return nome_semana
    elif numero_dia_semana ==5:
        nome_semana="Quinta"
        return nome_semana
    elif numero_dia_semana ==6:
        nome_semana="Sexta"
        return nome_semana
    elif numero_dia_semana ==7:
        nome_semana="Sábado"
        return nome_semana

resultado_numero_semana = digite_numero_dia_semana()
resultado_nome_dia_semana = exibe_dia(resultado_numero_semana)
print("O nome do dia é: ",resultado_nome_dia_semana)