from time import sleep

def maior (*num):
  cont = maior = 0
  print('Aanalisando os valores ')
  for valor in num:
     print(f'{valor}', end='', flush=True)
     sleep(0.3)


print('~'*20)
maior (2,1,3,4,5,6)