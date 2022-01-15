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


n = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print('{} x {} = {}'.format(n, c, n*c))


soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {} valor: '.format(c)))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print('Você informou {} números PARES e a soma foi {}.'.format(cont, soma))


ter = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
dec = ter + (10 - 1) * raz
for c in range(ter, dec + raz, raz):
    print('{}'.format(c), end=' → ' )
print('ACABOU')
'''

