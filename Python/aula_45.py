"""
Repetições
while (enquanto)
Executa um bloco de código enquanto a condição for verdadeira
loop infinito -> Quando a condição nunca é falsa
"""

qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas:
    coluna = 1

    while coluna <= qtd_colunas:
        print(f"{linha=} - {coluna=}")
        coluna += 1

    linha += 1
print("Fim do loop")
