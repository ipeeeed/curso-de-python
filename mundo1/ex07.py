'''
nome = str(input('Digite seu nome completo: '))
print('Seu nome em MAIÚSCULO é {}'.format(nome.upper()))
print('Seu nome em minúsculo é {}'.format(nome.lower()))
dividido = nome.split()
print('Seu nome tem ao todo {} letras'.format(len(''.join(dividido))))
print('Seu primeiro nome é {} e ele tem {} letras'.format(dividido[0], len(dividido[0])))


num = int(input('Informe um número: '))
uni = num // 1 % 10
dez = num // 10 % 10
cen = num // 100 % 10
mil = num // 1000 % 10
print('Unidade: {}'.format(uni))
print('Dezena: {}'.format(dez))
print('Centena: {}'.format(cen))
print('Milhar: {}'.format(mil))


cid = str(input('Em que cidade você nasceu? ')).strip()
cidade = cid.capitalize()
print('Santo' in cidade)


n = str(input('Qual é seu nome completo? '))
nome = n.lower()
print('Seu nome tem Santos? {}'.format('santos' in nome))


frase = str(input('Digite uma frase: ')).strip().lower()
print('A letra A aparece {} vezes na frase.'.format(frase.count('a')))
print('A primeira letra A apareceu na posição {}.'.format(frase.find('a')+1))
print('A última letra A apareceu na posição {}.'.format(frase.rfind('a')+1))
'''

n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))