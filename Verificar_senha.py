senha = 1234

# x = int(input('digite sua senha: '))

# if (x == 1234):
# print('senha correta')

# else:
# print('senha incorreta')

x = input('digite sua senha: ')

if len(x) == 4 and x.isdigit():
    if x == '1234':
        print('senha correta')

else:
    print('senha incorreta')