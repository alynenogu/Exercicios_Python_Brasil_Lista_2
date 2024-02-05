#Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. 
#O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
#Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores,
# sendo encerrado;
#Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
#Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

def pergunta_valor (mensagem):
    numero = float(input(mensagem))
    return numero




def verifica_valor_a(valor_a):
    if valor_a == 0:
        print("A equação não é do segundo grau")
    else:
        valor_b = pergunta_valor("Qual o valor de b? ")
        valor_c = pergunta_valor("Qual o valor de c? ")
        return valor_b ,valor_c
   
  

def calcula_equacao(valor_a,valor_b, valor_c):
     
   delta = valor_b**2 - 4*valor_a*valor_c

   return delta

def verifica_delta(delta):

    if delta < 0 :
        print("A equação não tem raizes")
    elif delta == 0:
        print("A equação possui apenas uma raiz real")
    elif delta > 0:
        print("A equação possui duas raizes real")



resultado_a = pergunta_valor("Qual o valor de a?")
resultado_b, resultado_c  = verifica_valor_a(resultado_a)
resposta_equacao = calcula_equacao(resultado_a,resultado_b,resultado_c)
resultado_delta = verifica_delta(resposta_equacao)
 





