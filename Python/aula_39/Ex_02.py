"""

Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada.
Ex: Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.

"""

hora = input('Digite a hora em números inteiros: ')

try:
  hora_inteiro = int(hora)
  
  if hora_inteiro >= 0 and hora_inteiro <= 11:
    print('Bom dia.')
  elif hora_inteiro >= 12 and hora_inteiro <= 17:
    print('Boa tarde.')
  elif hora_inteiro >= 18 and hora_inteiro <= 23:
    print('Boa noite.')

except:
  print('Não é um número inteiro.')