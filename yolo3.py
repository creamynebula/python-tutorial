# lambda retorna uma "função sem nome"
def testaLambda(x):
    """Função que retorna uma função que multiplica o input (y) por x
    """
    return lambda y: y*x


x3 = testaLambda(3)  # x3: f(x) = 3x
print(x3(12))
x4 = testaLambda(4)  # x4: f(x) = 4x
print(x4(12))


def linear(m, n):
    """
    linear cria uma função linear com coef angular m e coef linear n
    """
    return lambda x: m*x + n


print(linear.__doc__)  # isso vai imprimir a documentation string de linear
m, n = 3, 1
f1 = linear(m, n)  # f(x) = 3x + 1
print('f1(x) = linear(', m, ',', n, ')')
print('f1(2) tal que f1(x) = ', m, '*', 'x', '+', n, ':', f1(2))
print('f1(3) tal que f1(x) = ', m, '*', 'x', '+', n, ':', f1(3))
print('f1(4) tal que f1(x) = ', m, '*', 'x', '+', n, ':', f1(4))
print('\n')

m, n = 2, 9
f2 = linear(m, n)  # f(x) = 2x + 9
print('f2(x) = linear(', m, ',', n, ')')
print('f2(2) tal que f2(x) = ', m, '*', 'x', '+', n, ':', f2(2))
print('f2(3) tal que f2(x) = ', m, '*', 'x', '+', n, ':', f2(3))
print('f2(4) tal que f2(x) = ', m, '*', 'x', '+', n, ':', f2(4))
print('\n')

impares = [1, 3, 5, 7]
uns = [1, 1, 1, 1]
maisUns = [1, 1, 1, 1, 1]
zipped = list(zip(impares, uns, maisUns))
print(zipped)
print('\n')

vetor = [0]
for i in range(7):
    vetor.append(0)
print(vetor)
