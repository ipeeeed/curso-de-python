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


from datetime import date
ano = int(input('Que ano quer analisar? Caso queira o ano atual, digite "0". '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO'.format(ano))


n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))
if n1 > n2 and n1 > n3:
    print('O maior valor digitado foi {}'.format(n1))
if n2 > n1 and n2 > n3:
    print('O maior valor digitado foi {}'.format(n2))
if n3 > n1 and n3 > n2:
    print('O maior valor digitado foi {}'.format(n3))

if n1 < n2 and n1 < n3:
    print('O menor valor digitado foi {}'.format(n1))
if n2 < n1 and n2 < n3:
    print('O menor valor digitado foi {}'.format(n2))
if n3 < n1 and n3 < n2:
    print('O menor valor digitado foi {}'.format(n3))


sal = float(input('Qual é o salário do funcionário? R$'))
if sal <= 1250:
    aum = sal + (sal * 15 / 100)
else:
    aum = sal + (sal * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(sal, aum))


print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('Terceiro segmento: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os segmentos acima PODEM FORMAR triângulos')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo')
'''