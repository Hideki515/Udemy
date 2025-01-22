"""

Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou impar. Caso o usuário não digite um número 
inteiro, informe que não é um número inteiro.
  
"""

numero_inteiro = input("Digite um número inteiro: ")

try:
    numero_inteiro = int(numero_inteiro)
    
    par = numero_inteiro % 2
    
    if par == 0:
        print("Número par.")
    else:
        print("Número ímpar.")
except:
    print("Não é um número inteiro.")