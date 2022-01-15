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


num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        tot = tot + 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes.'.format(num, tot))
if tot == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')


frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
#inverso = junto[::-1] ----- pode substituir o <for>
for letra in range(len(junto) - 1, -1, -1):
    inverso = inverso + junto[letra]
print('O inverso de {} é {}.'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')


maior = 0
menor = 0
for ida in range(1, 8):
    ano = int(input('Em que ano a {}ª pessoa nasceu? '.format(ida)))
    if 2022 - ano < 18:
        menor = menor + 1
        print('Menor')
    elif 2022 - ano >= 18:
        maior = maior + 1
        print('Maior')
print('Ao todo tivemos {} pessoas maiores de idade.'.format(maior))
print('E também tivemos {} pessoas menores de idade'.format(menor))


maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {:.1f}Kg'.format(maior))
print('O menor peso lido foi de {:.1f}Kg'.format(menor))
'''

soma = 0
media = 0
maioridade = 0
nomevelho = ''
totmulher20 = 0
for c in range(1, 5):
    print(5*'=', '{}ª PESSOA'.format(c), 5*'=')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    soma = soma + idade
    media = soma / 4
    if c == 1 and sexo in 'Mm':
        maioridade = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridade:
        maioridade = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 = totmulher20 + 1
print('A média de idade do grupo é de {} anos.'.format(media))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridade, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totmulher20))