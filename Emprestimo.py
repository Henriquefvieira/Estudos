casa = int(input('Qual o valor da casa? '))
salario = int(input('Qual o valor do seu salario? '))
parcela = int(input('Em quantas parcelas? '))

valor_parcela = casa / parcela

if valor_parcela > salario * 0.3:
    print('O valor da prestação passa dos 30% do seu salario')
elif valor_parcela <= salario * 0.3:
    print('Parabéns, seu empréstimo foi aprovado. O valor da sua prestação é {:.2f}'.format(valor_parcela))
