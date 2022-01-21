'''
sexo = str(input('Informe seu sexo [M/F/T]: ')).strip().upper()[0]
while sexo not in 'MmFfTt':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))


print("""Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue advinhar qual foi?""")
from random import randint
n = int(input('Qual é seu palpite? '))
pc = randint(0, 10)
erro = 1
while n != pc:
    erro = erro + 1
    if pc > n:
        n = int(input("""Mais... Tente mais uma vez!
        Qual é seu palpite? """))
    elif pc < n:
        n = int(input("""Menos... Tente mais uma vez!
        Qual é seu palpite? """))
print('Acertou com {} tentativas. Parabéns, o PC pensou no número {}!'.format(erro, pc))


from time import sleep
opção = 0
pri = int(input('Primeiro valor: \033[31m'))
seg = int(input('\033[mSegundo valor: \033[31m'))
while opção != 5:
    print("""\033[m    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa""")
    opção = int(input('>>>>> Qual é a sua opção? \033[31m'))
    print('\033[m',15*'=-=')
    sleep(2)
    if opção == 1:
        print('\033[mA soma entre \033[33m{}\033[m e \033[33m{}\033[m é \033[33m{}'.format(pri, seg, (pri + seg)))
    elif opção == 2:
        print('\033[mO resultado entre \033[33m{}\033[m x \033[33m{}\033[m é \033[33m{}'.format(pri, seg, (pri * seg)))
    elif opção == 3:
        if pri > seg:
            maior = pri
        elif pri < seg:
            maior = seg
        else:
            maior = 'nenhum'
        print('\033[mEntre \033[33m{}\033[m e \033[33m{}\033[m o maior valor é \033[33m{}\033[m'.format(pri, seg, maior))
    elif opção == 4:
        print('\033[mInforme os números novamente!')
        pri = int(input('Primeiro valor: \033[31m'))
        seg = int(input('\033[mSegundo valor: \033[31m'))
    elif opção == 5:
        print('\033[mFinalizando...')
    else:
        print('\033[mOpção inválida. Tente novamente!')
    print('\033[m',15*'=-=')
sleep(2.4)
print('Fim do programa! Volte sempre!')


# Fatorial
"""
from math import factorial
num = int(input('Digite um número para calcular seu Fatorial: '))
fat = factorial(num)
print('O fatorial de {}! é {}'.format(num, fat))
"""

n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c
    c = c - 1
print('{}'.format(f))


pri = int(input('Primeiro termo: '))
raz = int(input('Razão da PA: '))
ter = pri
con = 1
tot = 0
mais = 10
while mais != 0:
    tot = tot + mais
    while con <= tot:
        print('{} → '.format(ter), end='')
        ter = ter + raz
        con = con + 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(tot))


n = int(input('Quantos termos você quer mostrar? '))
f = 0
r = 1
s = 0
print(f, end=' → ')
while n > 1:
    n = n - 1
    s = f
    f = f + r
    r = s
    print(f, end=' → ')
print('Fim')


#-----------------------------------------------------
# Fibonacci
0 = 0
0 = 0 + 1 == 1
1 = 0

0 = 1
1 = 1 + 0 == 1
0 = 1

1 = 1
1 = 1 + 1 == 2
1 = 1

1 = 2
2 = 2 + 1 == 3
1 = 2

2 = 3
3 = 3 + 2 == 5
2 = 3

3 = 5
5 = 5 + 3 == 8
3 = 5

5 = 8
8 = 8 + 5 == 13
5 = 8

8 = 13
13 = 13 + 8 == 21
8 = 13
#-----------------------------------------------------


n = r = c = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    r = r + n
    c = c + 1
    if n == 999:
        c = c - 1
        s = r - 999
print('Você digitou {} números e a soma entre eles foi {}.'.format(c, s))
'''

continuar = 'S'
contar = media = soma = maior = menor = 0
while continuar != 'N':
    n = int(input('Digite um número: '))
    if contar == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    contar = contar + 1
    soma = soma + n
    continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if continuar != 'S' and continuar != 'N':
        print('Opção invalida!')
        continuar = 'N'
media = soma / contar
print('''Você digitou {} números e a média foi {}
O maior valor foi {} e o menor valor foi {}.'''.format(contar, media, maior, menor))
