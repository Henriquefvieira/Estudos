x = 620
ano = x // 365
x = x % 365
mes = x // 30
x = x % 30
dias = x

#if (x > 365):
#    ano = x //365
#    x = x % 365

#if (x < 365):
#    mes = x // 30
#    x = x - 30




print('Anos', (ano),'Meses', (mes),'Dias', (dias))