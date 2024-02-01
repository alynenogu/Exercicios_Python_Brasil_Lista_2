#Faça um Programa que leia três números e mostre-os em ordem decrescente.

#Como eu trato quando digitam todos os números iguais?

def pergunta_numeros(mensagem):
    numero = float(input(mensagem))

    return numero

def verifica_ordem_primeiro_elemento(primeiro_numero,segundo_numero,terceiro_numero):

    if primeiro_numero > segundo_numero and primeiro_numero > terceiro_numero:
        return primeiro_numero
    if segundo_numero > primeiro_numero and segundo_numero > terceiro_numero:
        return segundo_numero
    if terceiro_numero > primeiro_numero and terceiro_numero > segundo_numero:
        return terceiro_numero

def verifica_ordem_segundo_elemento(primeiro_numero,segundo_numero,terceiro_numero):

    if primeiro_numero > segundo_numero and primeiro_numero < terceiro_numero:
        return primeiro_numero
    if segundo_numero > primeiro_numero and segundo_numero < terceiro_numero:
        return segundo_numero
    if terceiro_numero > primeiro_numero and terceiro_numero < segundo_numero:
        return terceiro_numero

def verifica_ordem_terceiro_elemento(primeiro_numero,segundo_numero,terceiro_numero):

    if primeiro_numero < segundo_numero and primeiro_numero < terceiro_numero:
        return primeiro_numero
    if segundo_numero < primeiro_numero and segundo_numero < terceiro_numero:
        return segundo_numero
    if terceiro_numero < primeiro_numero and terceiro_numero < segundo_numero:
        return terceiro_numero

resultado_primeiro_numero = pergunta_numeros("Digite o primeiro número: ")
resultado_segundo_numero = pergunta_numeros("Digite o segundo número: ")
resultado_terceiro_numero = pergunta_numeros("Digite o terceiro número: ")
primeiro_elemento = verifica_ordem_primeiro_elemento(resultado_primeiro_numero,resultado_segundo_numero,resultado_terceiro_numero)
segundo_elemento = verifica_ordem_segundo_elemento(resultado_primeiro_numero,resultado_segundo_numero,resultado_terceiro_numero)
terceiro_elemento = verifica_ordem_terceiro_elemento(resultado_primeiro_numero,resultado_segundo_numero,resultado_terceiro_numero)
print("A ordem descrescente é : ",primeiro_elemento," ",segundo_elemento," ",terceiro_elemento)