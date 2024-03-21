pessoas = []

while True:
    nome = input('Digite o nome da pessoa (ou "sair" para encerrar): ')

    if nome == 'sair':
        break

    pessoas.append(nome)

print('Pessoas cadastradas:')
for pessoa in pessoas:
    print(pessoa)