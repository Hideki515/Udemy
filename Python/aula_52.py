frase = (
    "O Python é uma linguagem de progração "
    "multiparadigma. "
    "Python foi criado por Guido van Rossum."
)

i = 0
apareceu_mais = 0
letra_mais_apareceu = ""
while i < len(frase):
    letra_atual = frase[i]
    quantas_vezes = frase.count(letra_atual)

    if letra_atual == " ":
        i += 1
        continue

    if apareceu_mais < quantas_vezes:
        apareceu_mais = quantas_vezes
        letra_mais_apareceu = letra_atual

    i += 1

print(
    f'A letra que mais apareceu foi "{letra_mais_apareceu}" com {apareceu_mais} vezes.'
)
