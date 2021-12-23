'''
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=-' * 20)
import random
num = random.randint(1, 3)
n = 2 #int(input('Em que número eu pensei? '))
from time import sleep
print('Prossessando...')
sleep(3)
if num != n:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(num, n))
else:
    print('PARABÉNS! Você conseguiu me vencer!')


vel = float(input('Qual é a velocidade do carro? '))
if vel > 80:
    mul = (vel - 80) * 7
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    print('Você deve pagar uma multa de R${:.2f}!'.format(mul))
print('Tenha um bom dia e dirija com segurança!')


n = int(input('Digite um número: '))
res = n % 2
if res != 0:
    print('ÍMPAR')
else:
    print('PAR')


d = float(input('Qual a distância da sua viagem? '))
if d <= 200:   
    p = d * 0.50
else:
    p = d * 0.45
print('Você está prestes a começar uma viagem de {}Km'.format(d))
print('E o preço da sua passagem será de R${:.2f}'.format(p))
'''

