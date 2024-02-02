#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos 
#são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 
#3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, 
#mas não é descontado (é a empresa que deposita). 
#O Salário Líquido corresponde ao Salário Bruto menos os descontos.
#O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#Desconto do IR:
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%
#Salário Bruto acima de 2500 - desconto de 20% 
#Imprima na tela as informações, dispostas conforme o exemplo abaixo. 
#No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#        Salário Bruto: (5 * 220)        : R$ 1100,00
#        (-) IR (5%)                     : R$   55,00  
#        (-) INSS ( 10%)                 : R$  110,00
#        FGTS (11%)                      : R$  121,00
#        Total de descontos              : R$  165,00
#        Salário Liquido                 : R$  935,00

def pergunta_horas():
    horas = int(input("Quantas horas o colaborador trabalhou esse mês? "))
    return horas

def pergunta_valor_hora():
    valor = float(input("Qual é o valor pago por hora desse colaborador? "))
    return valor

def define_salario_bruto(horas,valor):
    salario_bruto = horas*valor
    return salario_bruto

def desconto_sindicato(salario_bruto):
    desconto_sindicato = salario_bruto * 0.3
    return desconto_sindicato

def desconto_inss(salario_bruto):
    desconto_inss = salario_bruto * 0.10
    return desconto_inss

def desconto_fgts(salario_bruto):
    desconto_fgts = salario_bruto * 0.11
    return desconto_fgts

def desconto_ir(salario_bruto):

    if salario_bruto <=900:
        desconto_salario_bruto = 0
        return desconto_salario_bruto
    elif salario_bruto > 900 and salario_bruto <=1500:
        desconto_salario_bruto = salario_bruto*0.05
        return desconto_salario_bruto
    elif salario_bruto > 1500 and salario_bruto <=2500:
        desconto_salario_bruto = salario_bruto*0.10
        return desconto_salario_bruto
    elif salario_bruto > 2500:
        desconto_salario_bruto = salario_bruto*0.20
        return desconto_salario_bruto
    
def calcula_desconto(desconto_inss, desconto_ir):
    desconto_total = desconto_inss + desconto_ir
    return desconto_total

def calcula_salario_liquido(salario_bruto, desconto_total):
    salario_liquido = salario_bruto - desconto_total
    return salario_liquido

resultado_hora = pergunta_horas()
resultado_valor = pergunta_valor_hora()
resultado_salario = define_salario_bruto(resultado_hora,resultado_valor)
resultado_sindicato = desconto_sindicato(resultado_salario)
resultado_fgts = desconto_fgts(resultado_salario)
resultado_inss = desconto_inss(resultado_salario)
resultado_ir = desconto_ir(resultado_salario)
resultado_descontos = calcula_desconto( resultado_inss,resultado_ir)
resultado_salario_liquido = calcula_salario_liquido(resultado_salario,resultado_descontos)

print("Salário Bruto:  (",resultado_hora, "*", resultado_valor,") : R$",resultado_salario)    
print("(-) IR  ",resultado_ir)  
print("(-) INSS ( 10%)  ",resultado_inss)   
print("FGTS (11%)  : R$",resultado_fgts)  
print("Total de descontos  : R$",resultado_descontos)  
print(" Salário Liquido    : R$",resultado_salario_liquido)  

 
 
 