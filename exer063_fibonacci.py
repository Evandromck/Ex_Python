print('-'*30)
print('Sequência de fibonacci')
for c in range(0, 10):
    n = int(input('Quantos termos voce quer mostrar -> '))
    t1 = 0
    t2 = 1
    print('~'*30)
    print('{} -> {}'.format(t1, t2), end='')
    cont = 3
    while cont <= n:
        t3 = t1 + t2
        print(' -> {}'.format(t3), end='')
        t1 = t2
        t2 = t3
        cont += 1
    print(' fim ')
    print('~'*30) 
print('fim do fim')   