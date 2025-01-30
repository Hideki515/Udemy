"""
Repeticão
while (enquanto)
executa um bloco de código enquanto uma condição for verdadeira
loop infinito -> Quando um código não tem fim
"""

contador = 0

while contador < 10:
    contador += 1

    if contador == 5:
        print("Pulando o número 5")
        continue

    print(contador)
