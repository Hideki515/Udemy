"""
While / else 
"""

string = "Python"

i = 0
while i < len(string):
    letra = string[i]

    if letra == "t":
        break

    print(letra)
    i += 1

else:  # Executa quando o while termina sem interrupção
    print("Fim do while")
print("Fim do programa")
