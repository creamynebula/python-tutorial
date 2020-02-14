def mod5_x(x):
    return x % 5


vect1 = [100, 51, 14]
print('Que número é o maior em mod 5,', vect1, '?', max(vect1, key=mod5_x))
print('\n', help(max))
