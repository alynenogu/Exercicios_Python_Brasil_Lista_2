#As Organizações Tabajara resolveram dar um 
#aumento de salário aos seus colaboradores e lhe contraram para desenvolver o 
#programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, 
#baseado no salário atual:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.

def recebe_salario():
    salario = float(input("Digite o salário do colaborador: "))

    return salario

def define_percentual(salario):
    if salario < 280:
        percentual = 0.20
        return float(percentual)
    if salario>=280 and salario < 700:
        percentual = 0.15
        return float(percentual)
    if salario>=700 and salario < 1500:
        percentual = 0.10
        return float(percentual)
    if salario>=1500:
        percentual = 0.5
        return float(percentual)
    
def define_salario_reajustado (salario,percentual):
    salario_reajustado = (salario*percentual)+salario

    return salario_reajustado

resultado_salario = recebe_salario()
resultado_percentual = define_percentual(resultado_salario)
resultado_salario_reajustado = define_salario_reajustado(resultado_salario ,resultado_percentual)
print("Salário Anterior: ",resultado_salario)
print("Reajuste Aplicado: ",resultado_percentual)
print("Salário Reajustado: ",resultado_salario_reajustado)

