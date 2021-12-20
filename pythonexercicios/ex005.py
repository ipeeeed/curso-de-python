'''
n = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(n, int(n)))


from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
#hi = (co ** 2 + ca ** 2) ** (1/2)
#print('A hipotenusa vai medir {:.2f}'.format(hi))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))


from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tangente))


from random import choice
print('Digite o nome de alunos')
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
a5 = str(input('Quinto aluno: '))
a6 = str(input('Sexto aluno: '))
lis = [a1, a2, a3, a4, a5, a6]
sor = choice(lis)
print('O aluno escolhido foi {}'.format(sor))


from random import shuffle
print('Digite o nome de alunos')
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
a5 = str(input('Quinto aluno: '))
a6 = str(input('Sexto aluno: '))
lis = [a1, a2, a3, a4, a5, a6]
shuffle(lis)
print('A ordem de apresentação será: {}'.format(lis))
'''