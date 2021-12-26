nome = str(input('Qual o seu nome? '))
if nome == 'Pedro':
    print('Que nome bonito!')
elif nome == 'Gabriel' or nome == 'Maria' or nome == 'Paulo' or nome == 'João' or nome == 'José' or nome == 'Ana':
    print('Seu nome é bem popular no Brasil.')
elif nome == 'Claudio' or nome == 'Clóvis':
    print('Seu nome é engraçado.')
elif nome in 'Jéssica Juliana Bia Matheus':
    print('Ora Ora! Belo nome!')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia {}'.format(nome))
