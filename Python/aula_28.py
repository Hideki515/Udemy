'''
Interpolção básica de strings
s - string
d e i - int
f - float
x e X Hexadecimal
'''

nome = 'Hideki'
preco = 1000.1245221
variavel = '%s, o preço é R$%f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %08X' %(1500, 1500))