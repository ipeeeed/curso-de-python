nome = 'Pedro'
idade = 23
salário = 987.35
#print(f'O {nome:^10} tem {idade} anos e ganha R${salário:.2f}')

from time import sleep
cont = 0
while True:
    cont = cont + 1
    sleep(0.01)
    print(cont)
    if cont == 60:
        break