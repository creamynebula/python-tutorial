import math as math


def mod5_x(x):
    return x % 5


vect1 = [100, 51, 14]
print('\nQue número é o maior em (mod 5),', vect1, '?', max(vect1, key=mod5_x))
print('\n', help(max))


def truncate(number, n):
    return math.floor(number*10**n)/10**n


pi = 3.14159265359
x = truncate(pi, 5)

print('\nPi, 5 dígitos depois da vírgula:', x)


def quiz_message(grade):
    outcome = 'deu ruim' if grade < 60 else 'passou'
    print('\nSua situação final:', grade, outcome)


quiz_message(59)
quiz_message(61)
