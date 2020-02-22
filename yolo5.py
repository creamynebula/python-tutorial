animals = ['zebra', 'guaxinim', 'lontra', 'dragão']
chars = 0
for x in animals:
    chars += len(x)
print('Número de caracteres: {}    Tamanho médio: {}'.format(
    chars, chars/len(animals)))


# recebe [a0,a1,a2...,an-1] e retorna [a0,a2,a4,...]
def skip_elements(elements):
    enumerados = enumerate(elements)
    resultado = []
    for index, item in enumerados:
        if index % 2 == 0:
            resultado.append(item)
    return resultado


# Should be ['a', 'c', 'e', 'g']
print(skip_elements(["a", "b", "c", "d", "e", "f", "g"]))
# Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']))

lista1 = [('mateus', 'mateus.souzaaa@gmail.com'), ('fulano', 'fulano@sharklasers.com'),
          ('chihaya', 'karutafuru@karuta.net'), ('chitanda', 'chitandaeru@hyouka.jp')]

pessoas = []
for pessoa in lista1:
    pessoas.append('{} - {}'.format(pessoa[0], pessoa[1]))
print(pessoas)

x = 0.125
# retorna uma tuple (a,b) aonde a/b = x
numerator, denominator = x.as_integer_ratio()
print(numerator / denominator)

a = 1
b = 0
# em python podemos a,b = b,a pra inverter os valores, porque ele trata isso como (a,b) = (b,a)
a, b = b, a
print(a, b)


def select_second(L):
    """Return the second element of the given list. If the list has no second
    element, return None.
    """
    if len(L) > 1:
        return L[1]
    return None


def purple_shell(racers):
    """Given a list of racers, set the first place racer (at the front of the list) to last
    place and vice versa.

    >>> r = ["Mario", "Bowser", "Luigi"]
    >>> purple_shell(r)
    >>> r
    ["Luigi", "Bowser", "Mario"]
    """
    racers[0], racers[len(racers)-1] = racers[len(racers)-1], racers[0]


def fashionably_late(arrivals, name):
    """Given an ordered list of arrivals to the party and a name, return whether the guest with that
    name was fashionably late.
    """
    fashionable = len(arrivals) / 2
    last = len(arrivals) - 1
    when = arrivals.index(name)
    if when >= fashionable and when < last:
        return True
    return False
