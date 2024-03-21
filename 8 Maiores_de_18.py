maiores_de_18 = 0

for i in range(1, 11):
    idade = int(input(f'Digite a idade da {i}ª pessoa: '))

    if idade >= 18:
        maiores_de_18 += 1

print(f'Quantidade de pessoas maior ou igual a 18 anos: {maiores_de_18}')
