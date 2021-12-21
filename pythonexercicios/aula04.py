#Manipulação de Strings

frase = 'Curso em Vídeo Python'
'''
len(frase)                             >>> comprimento da frase
frase.count('o', 0, 21)                >>> destaca letra o na frase
frase.find('deo')                      >>> mostra onde começa a especificação da frase
frase.find('Android')                  >>> Se você mostra uma informação que não existe, retorna -1
'Curso' in frase                       >>> vai dizer se é true ou false a existência da especificação na frase
frase.replace('Python', 'Android')     >>> Substitui uma informação true por uma informação qualquer que você pode adicionar
frase.upper()                          >>> Transforma tudo em caixa alta
frase.lower()                          >>> Transforma tudo em caixa baixa
frase.capitalize()                     >>> Transforma a primeira letra em maiúscula e TODAS as outras em minúsculas
frase.title()                          >>> Cada palavra depois de um espaço transforma a primeira letra em maiúscula
'''

frase2 = '   Aprenda Python  '
#frase2.strip()                         >>> Vai retirar espaços vazios da frase
#frase2.rstrip()                        >>> retirar os espaços vazios da direita
#frase2.lstrip()                        >>> retirar os espaços vazios da esquerda

#frase.split()                          >>> Divide cada uma das palavras, gerando uma lista com numerações individuais
#'-'.join(frase)                        >>> Junta os strings divididos e adiciona uma marcação nova

print()