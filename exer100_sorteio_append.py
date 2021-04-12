import random import randint
from time import sleep

def sorteio(lista)
    print('Sorteio de 5 valores da lista: ', end='')
    for cont in range(0, 5):
       n =randint(1, 10)
       lista.append(n)
       print(f'{n}', end=', flush=true)

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor & 2 == 0