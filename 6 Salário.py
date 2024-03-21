# Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas, o valor que recebe por hora e calcula o salário desse funcionário. A seguir, mostre o número e o salário do funcionário, com duas casas decimais.
numero_funcionario = int(input("Digite o número do funcionário: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas: "))
valor_por_hora = float(input("Digite o valor que o funcionário recebe por hora: "))

salario = horas_trabalhadas * valor_por_hora

print("Número do funcionário:", numero_funcionario)
print("Salário do funcionário: R$", (salario))