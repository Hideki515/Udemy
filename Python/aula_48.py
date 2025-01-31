"""
Calculadora com while
"""

while True:
    print("Calculadora")

    sair = input("Deseja sair? [s]im ou [n]ão: ").lower().startswith("s")

    if sair is True:
        break
