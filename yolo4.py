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
    print('\nSua situação final:', grade, outcome, '\n')


quiz_message(59)
quiz_message(61)

lista1, lista2 = [1, 2, 4, 9, 6, 10, 11, 12], [1, 1, 2, 1]
print('lista 1 no começo:', lista1)
print('lista 2 no começo:', lista2)
lista1.append(13)
lista1.extend(lista2)
print('lista 1 dps de add "13" e os elementos de lista 2:', lista1)

# insert(i, elemento) insere elemento ANTES da posiçao i
lista1.insert(len(lista1)-1, 'penultimo')
print(lista1)

# remove o 1o elemento que tem esse valor, se nao tiver nenhum raises a ValueError
lista1.remove('penultimo')
print(lista1)

# lista1.pop(i) remove o elemento em i, ou remove o último se nao especificar índice, e retorna o elemento entao da pra assign to variable ou func
# len(lista1)-2 é o último elemento, porque se a lista tiver por ex. 10 elementos, len(lista1)-2 = índice 8, o penúltimo.
lista1.pop(len(lista1)-2)
print(lista1)

# lista1.clear() removeria todos os elementos da lista
# lista1.count(elemento) retorna o numero de vezes que elemento aparece
# lista.index(elemento) retorna o menor índice aonde elemento aparece

print('Quantidade de 1\'s:', lista1.count(1))
print('Index do elemento 6, se houver:', lista1.index(6))

lista1.sort()
print('Sorted:', lista1)

# primeiro a lista vazia
lista3 = []
# agora 1,4,9,16...
for x in range(19):
    lista3.append(x**2)
print('\nLista3:', lista3)

# ou
lista3 = list(map(lambda x: x**2, range(19)))
print('\nLista3 sem side effects:', lista3)

# ou, super fácil de ler e escrever
lista3 = [x**2 for x in range(19)]
print('\nLista3 sem side effects usando uma notacao r0x:', lista3)
print('Último elemento de lista3:', lista3[-1])
print('Últimos 3 elementos de lista3:', lista3[-3:])


def funcx(x):
    if x % 2 == 0:
        return x
    else:
        return x**3


lista4 = list(map(lambda x: funcx(x), range(19)))

print('\nLista4 sem side effects usando uma notacao r0x:', lista4)
print('Elementos da lista ordenados(com side effect, a lisat muda quando faz sorted(lista)):', sorted(lista4))
print('Lista 4:', lista4)
