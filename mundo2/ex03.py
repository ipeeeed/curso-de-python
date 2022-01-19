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
    else:
        print('\033[mOpção inválida. Tente novamente!')
    print('\033[m',15*'=-=')
print('Finalizando...')
sleep(2.4)
print('Fim do programa! Volte sempre!')
print('s')