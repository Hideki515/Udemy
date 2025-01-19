"""
Introdução ao try/except
try -> tentar executar o código
except -> caso ocorra um erro, executar o código

"""

numero_str = input('Digite um número: ')
  
try:
  
  print('STR: ', numero_str)
  
  numero_float = float(numero_str)

  print('FLOAT: ', numero_float)

  print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
  print('Você não digitou um número')