# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser verdadeiras.
# Se qualquer valor for considerado falso, a expressão
# será avaliada naquele valor
# São considerados falsy
# o o.o '' False
# Também existe o tipo None que é usado para representar
# um não valor

entrada = input('[E] - entrar [S] - sair')
senha_digitada = input('Senha: ')

senha = '123'

if entrada == "E" and senha_digitada == senha:
  print('Entrou')
else:
  print("Saiu")