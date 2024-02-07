#Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#Álcool:
#até 20 litros, desconto de 3% por litro
#acima de 20 litros, desconto de 5% por litro
#Gasolina:
#até 20 litros, desconto de 4% por litro
#acima de 20 litros, desconto de 6% por litro 
#Escreva um algoritmo que leia o número de litros vendidos, 
#o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
#calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o 
#preço do litro do álcool é R$ 1,90.

def pergunta_litros():
    litros = float(input("Quantos litros de combustível foram vendidos?"))

    return litros

def pergunta_combustivel():
    tipo_combustivel = input("Qual tipo de combustível foi vendido? A-álcool, G-gasolina ")
    return tipo_combustivel

def verifica_tipo_combustivel (tipo_combustivel,litros):

    if tipo_combustivel == "A":
       return calcula_alcool(litros)
    elif tipo_combustivel =="G":
       return  calcula_gasolina(litros)
    else:
        print("Ops, opção inválida")

def calcula_alcool(litros): 
#Álcool:
#até 20 litros, desconto de 3% por litro
#acima de 20 litros, desconto de 5% por litro
    litro_ate_20 = (1.90*0.03)
    litro_acima_20 = (1.90*0.05)

    if litros <= 20:
        gasto = litro_ate_20 * litros
        return gasto 
    elif litros > 20:
        gasto = litro_acima_20 * litros
        return gasto 


def calcula_gasolina(litros):
#Gasolina:
#até 20 litros, desconto de 4% por litro
#acima de 20 litros, desconto de 6% por litro
    litro_ate_20 = (2.50*0.04)
    litro_acima_20 = (2.50*0.06)

    if litros <= 20:
        gasto = litro_ate_20 * litros
        return gasto 
    elif litros > 20:
        gasto = litro_acima_20 * litros
        return gasto 
    
resultado_litros = pergunta_litros()
resultado_tipo_gasolina = pergunta_combustivel()
print(resultado_litros," ",resultado_tipo_gasolina)
resultado_gasto = verifica_tipo_combustivel (resultado_tipo_gasolina,resultado_litros)

print ("O valor gasto foi: R$", resultado_gasto)