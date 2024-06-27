# if / elif      /else
# se / se não se / se não

entrada = input('Você quer "entrar" ou "sair"? ')
# or -> É um operador lógico que é utilizado para realizar operações de comparação entre expressões booleanas.
if entrada == 'entrar' or entrada == 'Entrar':
  print('Você entrou no sistema')
elif entrada == 'sair' or entrada == 'Sair':
  print('Você saiu do sistema')
else:
  print('Você não digitou sem entrar nem sair')