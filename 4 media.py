# Leia 2 valores de ponto flutuante de dupla precisão A e B, que correspondem a 2 notas de um aluno. A seguir, calcule a média do aluno, sabendo que a nota A tem peso 3.5 e a nota B tem peso 7.5 (A soma dos pesos portanto é 11). Assuma que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.
nota_A = float(input("Digite a primeira nota (de 0 a 10.0): "))
nota_B = float(input("Digite a segunda nota (de 0 a 10.0): "))

media = (nota_A + nota_B) / 2

print("Média do aluno:", (media, ))