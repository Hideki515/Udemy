"""
Calculadora com while
"""

while True:
    numero_1 = input("Digite o primeiro número: ")
    numero_2 = input("Digite o segundo número: ")
    operador = input("Digite o operador: ")

    numeros_validos = None

    try:
        numero_1_valido = float(numero_1)
        numero_2_valido = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print("Digite um número válido.")
        continue

    operadores_permitidos = "+-*/"

    if operador not in operadores_permitidos:
        print("Digite um operador válido.")
        continue

    if len(operador) > 1:
        print("Digite apenas um operador.")
        continue

    sair = input("Deseja sair? [s]im ou [n]ão: ").lower().startswith("s")

    if sair is True:
        break
