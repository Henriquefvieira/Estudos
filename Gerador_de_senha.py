import random

#N1 = ['1,' '2', '3', '4,' '5', '6', '7,' '8', '9', '0']
#N2 = ['1,' '2', '3', '4,' '5', '6', '7,' '8', '9', '0']
#N3 = ['1,' '2', '3', '4,' '5', '6', '7,' '8', '9', '0']
#N4 = ['1,' '2', '3', '4,' '5', '6', '7,' '8', '9', '0']
#N5 = ['1,' '2', '3', '4,' '5', '6', '7,' '8', '9', '0']
#N6 = ['1,' '2', '3', '4,' '5', '6', '7,' '8', '9', '0']

N1 = random.randint(0, 9)
N2 = random.randint(0, 9)
N3 = random.randint(0, 9)
N4 = random.randint(0, 9)
N5 = random.randint(0, 9)
N6 = random.randint(0, 9)

#senha = (N1, N2, N3, N4, N5, N6)
#def senha(N1, N2, N3, N4, N5, N6):
    #return random.choice(N1)

#print('sua senha é:' (senha))

print('sua senha é:', (N1, N2, N3, N4, N5, N6))
print('sua senha é:', (N1), (N2), (N3), (N4), (N5), (N6))