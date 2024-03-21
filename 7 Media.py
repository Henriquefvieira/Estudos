N1 = float(input('primeira nota: '))
N2 = float(input('segunda nota: '))
N3 = float(input('terceira nota: '))
N4 = float(input('quarta nota: '))

media = (N1 + N2 + N3 + N4) / 4

print('media do aluno:', (media))

if media >= 7.0:
    print('aluno aprovado')
elif media < 5.0:
    print('aluno reprovado')
else:
    print('aluno de recuperação')