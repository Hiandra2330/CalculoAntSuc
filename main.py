entrada = input('digite um numero (ou "sair" para encerrar)\n')
while entrada != 'sair': 
  numero = int(entrada)

  ant = numero -1
  suc = numero +1

  print('o sucessor de ' + str(numero) + ' é ' + str(suc)) 
  print('o antecessor de ' + str(numero) + ' é ' + str(ant))
  entrada = input('digite um numero (ou "sair" para encerrar)\n') 
print('programa encerrado!')