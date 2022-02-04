n1 = 0
n2 = 0
esc = ""
while True:
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite outro número: "))
    esc = int(input("""Escolha a opção:
    1 - Somar
    2 - Subtrair
    3 - Multiplicar
    4 - Dividir
    0 - Sair
    """))
    if esc == 0:
        print("Até logo!")
        break
    else:
        if esc == 1:
            n3 = n1 + n2
            print(f"{n1} mais {n2} é igual a {n3}.")
        elif esc == 2:
            n3 = n1 - n2
            print(f"{n1} menos {n2} é igual a {n3}.")
        elif esc == 3:
            n3 = n1 * n2
            print(f"{n1} vezes {n2} é igual a {n3}.")
        elif esc == 4:
            n3 = n1 / n2
            print(f"{n1} dividido por {n2} é igual a {n3}.")
        else:
            print("Opção invalida, programa será descontinuado!")
            break
    print("-"*50)
    sair = int(input("""Deseja continuar?
    0 - Sim
    1 - Não
    """))
    if sair == 0:
        n1 = n2 = 0
    elif sair == 1:
        print("Até logo!")
        break
    else:
        print("Opção invalida, programa será descontinuado!")
        break
    print("-"*50)
print("Fim do programa!")
