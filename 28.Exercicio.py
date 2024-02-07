#O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                      Até 5 Kg           Acima de 5 Kg
#File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
#Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
#Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
#Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, 
#porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente
#receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade
#de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: 
#tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

def pergunta_tipo_carne():
    tipo_carne = input("Qual o tipo da carne? F - File Duplo, A - Alcatra, P - Picanha ")
    return tipo_carne

def pergunta_kg_carne():
    KG_carne = float(input("Quantos KG : "))
    return KG_carne

def verifica_tipo_carne (tipo_carne,KG_carne):

    if tipo_carne == "F":
       return calcula_File(KG_carne)
    elif tipo_carne =="A":
       return  calcula_Alcatra(KG_carne)
    elif tipo_carne =="P":
       return  calcula_Picanha(KG_carne)
    else:
        print("Ops, opção inválida")

def calcula_File(KG_carne): 
    valor_kg_ate_5 = 4.90
    valor_kg_acima_5 = 5.80

    if KG_carne <= 5:
        valor_total_kg = valor_kg_ate_5*KG_carne
        return valor_total_kg
    elif KG_carne > 5:
        valor_total_kg = valor_kg_acima_5*KG_carne
        return  valor_total_kg

def calcula_Alcatra(KG_carne): 
    valor_kg_ate_5 = 5.90
    valor_kg_acima_5 = 6.80

    if KG_carne <= 5:
        valor_total_kg = valor_kg_ate_5*KG_carne
        return valor_total_kg
    elif KG_carne > 5:
        valor_total_kg = valor_kg_acima_5*KG_carne
        return  valor_total_kg
    
def calcula_Picanha(KG_carne): 
    valor_kg_ate_5 = 6.90
    valor_kg_acima_5 = 7.80

    if KG_carne <= 5:
        valor_total_kg = valor_kg_ate_5*KG_carne
        return valor_total_kg
    elif KG_carne > 5:
        valor_total_kg = valor_kg_acima_5*KG_carne
        return  valor_total_kg

def pergunta_tipo_de_pagamento():
    tipo_pagamento = input("Qual o tipo de pagamento? D - dinheiro ou C - Cartão Tabajara ")
    
    return tipo_pagamento

def verifica_tipo_desconto (tipo_pagamento,valor_total_kg):
    valor_desconto = 0
    if tipo_pagamento == "D":
       return valor_desconto
    elif tipo_pagamento =="C":
        valor_desconto = (valor_total_kg*0.05)
        return valor_desconto
    else:
        print("Ops, opção inválida")

def calcula_pagamento (tipo_pagamento,valor_total_kg,valor_desconto):

    if tipo_pagamento == "D":
       
       return valor_total_kg
    elif tipo_pagamento =="C":
        valor_total_kg = valor_total_kg - valor_desconto
        return valor_total_kg
    else:
        print("Ops, opção inválida")



resultado_tipo_carne = pergunta_tipo_carne()
resultado_kg = pergunta_kg_carne()
resultado_valor_reais = verifica_tipo_carne (resultado_tipo_carne,resultado_kg)
print("Valor Gasto em Carne R$:", resultado_valor_reais)
resultado_tipo_pagamento = pergunta_tipo_de_pagamento()
resultado_tipo_desconto = verifica_tipo_desconto(resultado_tipo_pagamento,resultado_valor_reais)
print("Valor Desconto R$:", round(resultado_tipo_desconto,2))
resultado_valor_com_desconto = calcula_pagamento (resultado_tipo_pagamento,resultado_valor_reais,resultado_tipo_desconto)
print("Valor com Desconto R$:", round(resultado_valor_com_desconto,2))