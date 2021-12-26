"""
nome = input('Digite seu nome: ')
print('Bem vindo(a) {:-^20}!'.format(nome))


n = int(input('Digite um número: '))
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}.'.format(n, n-1, n+1))


n = int(input('Digite um número: '))
print('O dobro de {} vale {}.'.format(n, n*2))
print('O triplo de {} vale {}.'.format(n, n*3))
print('A raiz quadrada de {} é igual a {}.'.format(n, n**(1/2)))


n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
#nf = (n1+n2)/2
print('A média entre {} e {} é igual a {}'.format(n1, n2, (n1+n2)/2))


n = float(input('Digite uma distância em metros: '))
print('A medida de {}m corresponde a'.format(n))
print('{}km'.format(n/1000))
print('{}hm'.format(n/100))
print('{}dam'.format(n/10))
print('{}dm'.format(n*10))
print('{}cm'.format(n*100))
print('{}mm'.format(n*1000))


n = int(input('Digite um número para ver sua tabuada: '))
print('-' * 15)
print('{} x  1 = {}'.format(n, n*1))
print('{} x  2 = {}'.format(n, n*2))
print('{} x  3 = {}'.format(n, n*3))
print('{} x  4 = {}'.format(n, n*4))
print('{} x  5 = {}'.format(n, n*5))
print('{} x  6 = {}'.format(n, n*6))
print('{} x  7 = {}'.format(n, n*7))
print('{} x  8 = {}'.format(n, n*8))
print('{} x  9 = {}'.format(n, n*9))
print('{} x 10 = {}'.format(n, n*10))
print('-' * 15)


n = float(input('Quanto dinheiro você tem na carteira? R$'))
print('Com R${:.2f} você pode comprar US${:.2f}.'.format(n, (n/3.27)))


Lar = float(input('Largura da parede: '))
Alt = float(input('Altura da parede: '))
Area = Lar*Alt
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(Lar, Alt, Area))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(Area*(1/2)))


n = float(input('Qual é o preço do produto? R$'))
print('O produto custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(n, n-(n*5/100)))


n = float(input('Qual é o salário do funcionário? R$'))
print('Um funcionário qua ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(n, n+(n*15/100)))


t = float(input('Informe a temperatura em C: '))
print('A temperatura de {}C corresponde a {}F!'.format(t, 9*t/5+32))


d = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
pago = (d*60) + (km*0.15)
print('O valor a pagar é de R${:.2f}!'.format(pago))
"""