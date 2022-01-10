'''
from time import sleep
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('BUM! BUM! POOOW!')


for c in range(2, 51, 2):
    if c % 2 == 0:
        print(c, end=' ')
print('Acabou!')


soma = 0
contador = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        contador = contador + 1
        soma = soma + c
#        print(c, end=' ')
print('A soma de todos os {} valores solicitados é de {}.'.format(contador, soma))
'''


for c in range():