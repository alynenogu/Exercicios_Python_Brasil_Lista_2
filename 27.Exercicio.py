#Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                      Até 5 Kg           Acima de 5 Kg
#Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
#Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, 
#receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) 
#de morangos e a quantidade (em Kg) 
#de maças adquiridas e escreva o valor a ser pago pelo cliente.

def pede_kg_morango():
    qtd_morango = float(input("Digite quantos kg de morangos? "))
    return qtd_morango

def pede_kg_maca():
    qtd_maca = float(input("Digite quantos kg de maçã? "))
    return qtd_maca

def verifica_morango(qtd_morango):
    valor_kg_ate_5 = 2.50
    valor_kg_acima_5 = 2.20
    if qtd_morango <= 5:
        valor_total_morango = valor_kg_ate_5*qtd_morango
        return valor_total_morango
    elif qtd_morango > 5:
        valor_total_morango = valor_kg_acima_5*qtd_morango
        return valor_total_morango

def verifica_maca(qtd_maca):
    valor_kg_ate_5 = 1.80
    valor_kg_acima_5 = 1.50
    if qtd_maca <= 5:
        valor_total_maca = valor_kg_ate_5*qtd_maca
        return valor_total_maca
    elif qtd_maca > 5:
        valor_total_maca = valor_kg_acima_5*qtd_maca
        return valor_total_maca
    
resposta_morango = pede_kg_morango()
resposta_maca = pede_kg_maca()
gasto_morango = verifica_morango(resposta_morango)
gasto_maca = verifica_maca(resposta_morango)
print("Gasto total com morango R$ ",gasto_morango)
print("Gasto total com maçã R$ ",gasto_maca)