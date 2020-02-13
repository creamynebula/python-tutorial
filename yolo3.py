# lambda retorna uma "função sem nome"
def testaLambda(x):
    """Função que retorna uma função que multiplica o input (y) por x
    """
    return lambda y: y*x


x3 = testaLambda(3)  # x3: f(x) = 3x
print('\nx3(12):', x3(12))
x4 = testaLambda(4)  # x4: f(x) = 4x
print('x4(12:', x4(12))


def linear(m, n):
    """
    linear(m,n) cria uma função linear com coef angular 'm' e coef linear 'n' fazendo lambda x: m*x + n

    exemplo:
    f1 = linear(7,9)
    f1(2) -> 23
    """
    return lambda x: m*x + n


# isso vai imprimir a documentation string de linear
print('\ndocstring de linear:', linear.__doc__)
m, n = 3, 1
f1 = linear(m, n)  # f(x) = 3x + 1
print('\nf1(x) = linear(', m, ',', n, ')', sep='')
print('f1(2) tal que f1(x) = ', m, '*', 'x', ' + ', n, ': ', f1(2), sep='')
print('f1(3) tal que f1(x) = ', m, '*', 'x', ' + ', n, ': ', f1(3), sep='')
print('f1(4) tal que f1(x) = ', m, '*', 'x', ' + ', n, ': ', f1(4), sep='')

m, n = 2, 9
f2 = linear(m, n)  # f(x) = 2x + 9
print('\nf2(x) = linear(', m, ',', n, ')', sep='')
print('f2(2) tal que f2(x) = ', m, '*', 'x', ' + ', n, ': ', f2(2), sep='')
print('f2(3) tal que f2(x) = ', m, '*', 'x', ' + ', n, ': ', f2(3), sep='')
print('f2(4) tal que f2(x) = ', m, '*', 'x', ' + ', n, ': ', f2(4), sep='')

impares = [1, 3, 5, 7]
uns = [1, 1, 1, 1]
maisUns = [1, 1, 1, 1, 1]
zipped = list(zip(impares, uns, maisUns))
print('\nzipped:', zipped)
print('\n')

vetor = [0]
for i in range(7):
    vetor.append(0)
print(vetor)

print(type(impares))
print(max(1, 2, 3))
print(min(1, 2, 3))
print(help(abs))
print(help(print))


def least_difference(a, b, c):
    diff1 = abs(b-c)
    diff2 = abs(a-c)
    diff3 = abs(a-b)
    return min(diff1, diff2, diff3)


print(least_difference(1, 5, 15))


def greet(who='mateus'):
    print('hi ', who)
