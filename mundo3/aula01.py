#lanche = 'hamburguer', 'suco', 'batata frita', 'pizza', 'pudim'
lanche = ('hamburguer', 'suco', 'batata frita', 'pizza', 'pudim')

'''
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

print('-'*30)

for comida in lanche:
    print(f'Eu vou comer {comida}')

print('-'*30)

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print('-'*30)
print(f'Eu vou comer mais \033[33m{lanche[0]}\033[m')
print(f'Gostei mais de \033[31m{lanche[0:2]}\033[m')
'''

#print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
#print(len(c)) #Lê quantos elementos tem dentro da tupla
#print(c.count(5)) #Conta quantos elementos específicos tem dentro da tupla
#print(c.index(5, 4)) #Mostra a posição do elemento específico a partir da posição marcada

pessoa = ('Pedro', 23, 'M', 60.00)
del(pessoa)
print(pessoa)