"""
Iterando strings com while
"""

#       012345678910
nome = "Bruno Hideki"  # Iteráveis

tamanho_nome = len(nome)

novo_nome = ""
contador = 0
while contador < tamanho_nome:
    print(f"{nome[contador]}")

    letra = nome[contador]
    novo_nome += f"{letra}_"

    contador += 1

print(f"{novo_nome=}")
