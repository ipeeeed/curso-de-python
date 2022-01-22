''''''
ext = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
n = int(input('Digite um número entre 0 e 20: '))
for contador, numero in enumerate(ext):
    if n == contador:
        n = numero
        break
#    print(f'O número {contador} é contado como {numero}')
print(f'O numero é o {n}')
