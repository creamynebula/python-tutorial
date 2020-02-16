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

lista1, lista2 = [1, 2, 4, 9, 6, 10, 11, 12], [1, 1, 1, 1]
lista1.append(13)
lista1.extend(lista2)
# insert(i, elemento) insere elemento ANTES da posiçao i
lista1.insert(len(lista1)-1, 'penultimo')
print(lista1)
# remove o 1o elemento que tem esse valor, se nao tiver nenhum retorna ValueError
lista1.remove('penultimo')
# lista1.pop(i) remove o elemento em i, ou remove o último se nao especificar índice
lista1.pop(len(lista1)-1)
print(lista1)
