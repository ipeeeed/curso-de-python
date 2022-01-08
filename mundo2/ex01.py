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


n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1, n2, m))
if m >= 7:
    print('O aluno está APROVADO.')
elif m < 7 and m >= 5:
    print('O aluno está em RECUPERAÇÃO.')
else:
    print('O aluno está REPROVADO.')


ano = int(input('Ano de nascimento: '))
idade = 2021 - ano
if idade <= 9:
    cat = 'MIRIM'
elif idade > 9 and idade <= 14:
    cat = 'INFANTIL'
elif idade > 14 and idade <= 19:
    cat = 'JUNIOR'
elif idade > 19 and idade <= 25:
    cat = 'SÊNIOR'
else:
    cat = 'MASTER'
print('O atleta tem {} anos.'.format(idade))
print('Classificação: {}'.format(cat))


pri = int(input('Primeiro segmento: '))
seg = int(input('Segundo segmento: '))
ter = int(input('Terceiro segmento: '))
if pri + seg < ter or seg + ter < pri or ter + pri < seg:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo')
elif pri != seg != ter != pri:
    print('Os segmentos acima PODEM FORMAR um triângulo ESCALENO')
elif pri == seg == ter:
    print('Os segmentos acima PODEM FORMAR um triângulo EQUILÁTERO')
elif pri == seg and pri != ter or seg == ter and seg != pri or ter == pri and ter != seg:
    print('Os segmentos acima PODEM FORMAR um triângulo ISÓSCELES')


peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal.')
elif imc >= 18.5 and imc < 25:
    print('PARABÉNS, você está na faixa de PESO NORMAL.')
elif imc >= 25 and imc < 30:
    print('Você está em SOBREPESO')
elif imc >= 30 and imc < 40:
    print('Você está em OBESIDADE!')
else:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')


print('{:=^40}'.format(' Lojas IPED '))
preço = float(input('Preço das compras: R$'))
print("""
FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
""")
opção = int(input('Qual a opção? '))
if opção == 1:
    total = preço - (preço * (10 / 100))
elif opção == 2:
    total = preço - (preço * (5 / 100))
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opção == 4:
    total = preço + (preço * (20 / 100))
    totalparc = int(input('Quantas parcelas? '))
    parcela = total / totalparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totalparc, parcela))
else:
    total = preço
    print('[ERRO] Opção invalida de pagamento. Tente novamente!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))
'''

import random
from time import sleep
print("""Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA""")
itens = ('Pedra', 'Papel', 'Tesoura')
jogador = int(input('Qual é a sua jogada? '))
jokenpo = random.randint(0, 2)
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!  ---->  {}'.format(jokenpo))
sleep(1)
if jogador == jokenpo:
    print('EMPATE!!')
elif jogador == 0 and jokenpo == 1 or jogador == 1 and jokenpo == 2 or jogador == 2 and jokenpo == 0:
    print('Computador GANHOU!')
elif jokenpo == 0 and jogador == 1 or jokenpo == 1 and jogador == 2 or jokenpo == 2 and jogador == 0:
    print('Jogador GANHOU!')
else:
    print('[ERRO] Informação invalida, tente novamente!')
print('Computador jogou {} e Jogador jogou {}'.format(itens[jokenpo], itens[jogador]))
