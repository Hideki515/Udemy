# Números não necessitam de aspas
# , é utilizada para mostrar mais de um valor
print(12, 34)

# String é necessario colocar aspas
print('Teste')

# sep -> serve para mudar o separador em argumentos não nomeados
# Separa os valores com /
print(25, 45, 43, sep='/')

# \r\n -> CRLF
# \n -> LF
# São utilizados para quebra de linha

# end -> final da linha ou para quebra de linha
# Separa os valores com / e \n quebra a linha
print(25, 45, sep='/', end=("\n"))
# Separa os valores com , e \n quebra a linha e coloca dois #
print(25, 45, sep=',', end=("\n##"))
# Separa os valores com - e coloca dois ## no final das linhas
print(25, 45, sep='-', end=("##"))