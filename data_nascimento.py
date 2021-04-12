ano = 2021
for c in range(1, 7):
    data = int(input('Digite a data'))
     ano = data - ano
     if ano > 18:
        maior += 1
     else:
         manor +=1   

print(f'tamos {maior} pessoas de maior')
print(f'temos {manor} pessoas de menor' )