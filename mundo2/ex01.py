#Exercícios de Condições Aninhadas

'''
valor = float(input('Valor da casa R$'))
salário = float(input('Salário do comprador R$'))
financiamento = int(input('Quantos anos de financiamento? '))
prestação = valor / (financiamento * 12)
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}'.format(valor, financiamento, prestação))
if prestação >= salário * (30 / 100):
    print('Acesso NEGADO!')
else:
    print('Acesso CONCEDIDO!')


num = int(input('Digite um número inteiro: '))
print("""Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL
""")
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} Convertido para BINÁRIO é igual a {}'.format(num, bin(num) [2:]))
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num) [2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num) [2:]))
else:
    print('Opção inválida. Tente novamente.')


n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('O PRIMEIRO valor é maior')
elif n1 < n2:
    print('O SEGUNDO valor é maior')
else:
    print('NÃO EXISTE valor maios, os dois são iguais')
'''

ano = int(input('Ano de nascimento: '))
data = 2021
idade = data - ano
print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade, data))
if idade < 18:
    print('Ainda faltam {} anos para o alistamento.'.format(18 - idade))
    print('Seu alistamento será em {}.'.format((18 - idade) + data))
elif idade > 18:
    print('Você já deveria ter se alistado há {} anos.'.format(idade - 18))
    print('Seu alistamento foi em {}.'.format(data - (idade - 18)))
else:
    print('Você tem que se alistar IMEDIATAMENTE!')
