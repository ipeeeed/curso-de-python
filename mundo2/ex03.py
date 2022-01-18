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
'''

opção = 0
while opção != 5:
    print("""
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa""")
    opção = int(input('Qual é a sua opção? '))
from time import sleep
print('Finalizando...')
sleep(2.4)
print('Fim do programa! Volte sempre!')
