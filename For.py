numero = int(input('Digite o número que você quer a tabuada: '))

print(f'Tabuada do {numero}:')

for i in range(1, 11):
    resultado = numero * i
    print(f'{numero} x {i} = {resultado}')
