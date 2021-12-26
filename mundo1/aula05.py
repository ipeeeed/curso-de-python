'''
tempo = int(input('Quantos anos tem seu carro? '))

#print('carro novo'if tempo <= 3 else'carro velho') #Simplificado

if tempo <= 3:
    print('carro novo')
else:
    print('carro velho')
'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('Sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua nota foi ruim! ESTUDE MAIS!')