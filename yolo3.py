#lambda retorna uma "função sem nome"
def testaLambda(x):
    """Função que retorna uma função que multiplica o input (y) por x
    """
    return lambda y: y*x

x3 = testaLambda(3) #x3: f(x) = 3x
print(x3(12))
x4 = testaLambda(4) #x4: f(x) = 4x
print(x4(12))

def f2(m, n):
    """
    f2 cria uma função linear com coef angular m e coef linear n
    """
    return lambda x: m*x + n

print(f2.__doc__) #isso vai imprimir a documentation string de f2
m,n=3,1
teste = f2(m,n) #f(x) = 3x + 1
print ('teste(2) tal que teste(x) = ',m,'*','x','+',n,':', teste(2))
print ('teste(3) tal que teste(x) = ',m,'*','x','+',n,':', teste(3))
print ('teste(4) tal que teste(x) = ',m,'*','x','+',n,':', teste(4))


m,n=2,9
teste = f2(m,n) #f(x) = 2x + 9
print ('teste(2) tal que teste(x) = ',m,'*','x','+',n,':', teste(2))
print ('teste(3) tal que teste(x) = ',m,'*','x','+',n,':', teste(3))
print ('teste(4) tal que teste(x) = ',m,'*','x','+',n,':', teste(4))
#esse comment eh soh pra testar o git push