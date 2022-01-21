'''
v = c = s = 0
while True:
    v = int(input('Digite um valor (999 para parar): '))
    if v == 999:
        break
    c = c + 1
    s = s + v
print(f'A soma dos {c} valores foi {s}!')


v = r = s = 0
t = 10
while True:
    s = 0
    v = int(input('Quer ver a tabuada de qual valor? ')) #para parar o programa insira um número negativo
    if v < 0:
        break
    t = t - 1
    while s != 10:
        s = s + 1
        r = s * v
        print(f'{v} x {s} = {r}')
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')


from time import sleep
from random import randint
print('=-'*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*20)
vitória = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            vitória = vitória + 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            vitória = vitória + 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {vitória} vezes.')


print('='*30)
print('CADASTRE UMA PESSOA')
print('='*30)
dezoito = vinte = homem = mulher = 0
while True:
    idade = int(input('Idade: '))
    if idade > 18:
        dezoito = dezoito + 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if sexo == 'M':
        homem = homem + 1
    elif sexo == 'F':
        if idade < 20:
            vinte = vinte + 1
        mulher = mulher + 1
    print('-'*30)
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar: [S/N] ')).strip().upper()[0]
    print('-'*30)
    if cont == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {dezoito}')
print(f'Ao todo temos {homem} homens cadastrados.')
print(f'E temos {vinte} mulheres com menos de 20 anos')


print('='*30)
print('SUPER LOJÃO DO IPED')
print('='*30)
produto = continua = baratíssimo = ''
preço = total = caro = barato = 0
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    if preço > 1000:
        caro = caro + 1
    if barato == 0: #or preço < barato
        barato = preço
        baratíssimo = produto
    else:
        if preço < barato:
            barato = preço
            baratíssimo = produto
    total = total + preço
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continua == 'N':
        break
print(f"""O total da compra foi R${total:.2f}
Temos {caro} produtos custando mais de R$1000.00
O produto mais barato foi {baratíssimo} que custa R${barato:.2f}""")
'''

print('='*30)
print('{:^30}'.format('BANCO Santo André'))
print('='*30)
valor = int(input('Que valor você quer sacar? R$ '))
total = valor
céd = 50
totalcéd = 0
while True:
    if total >= céd:
        total = total - céd
        totalcéd = totalcéd + 1
    else:
        if totalcéd > 0:
            print(f'Total de {totalcéd} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totalcéd = 0
        if total == 0:
            break
print('='*30)
print('Volte sempre ao BANCO Santo André. Tenha um bom dia!')
print('='*30)
