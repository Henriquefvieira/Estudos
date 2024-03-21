nome = str(input('Qual o seu nome?  '))
if nome == 'Henrique':
    print('Que Nome bonito!')
elif nome == 'Bruno' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é popular')
elif nome in 'Ana Marcia  julia':
    print('Belo nome feminino')
else:
    print('Seu nome é normal')
print('Tenha um bom dia, {}'.format(nome))