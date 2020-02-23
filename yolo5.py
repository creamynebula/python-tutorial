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


planets = ['Mercury', 'Venus', 'Earth', 'Mars',
           'Jupiter', 'Saturn', 'Uranus', 'Neptune']
short_planets = [planet for planet in planets if len(
    planet) < 7]  # planets com tamanho < 7
print(short_planets)
# planetas em maiúsculo + '!!'
loud_short_planets = [planet.upper() + '!!' for planet in short_planets]
print(loud_short_planets)


def has_lucky_number(nums):
    """Return whether the given list of numbers is lucky. A lucky list contains
    at least one number divisible by 7.
    """
    if len(nums) > 0:
        for num in nums:
            if num % 7 == 0:
                return True
    return False


def elementwise_greater_than(L, thresh):
    """Return a list with the same length as L, where the value at index i is 
    True if L[i] is greater than thresh, and False otherwise.

    >>> elementwise_greater_than([1, 2, 3, 4], 2)
    [False, False, True, True]
    """
    result = []
    for x in L:
        if x > thresh:
            result.append(True)
        else:
            result.append(False)
    return result


# mesma coisa, mto mais inteligente...
def elementwise_greater_than2(L, thresh):
    res = []
    for ele in L:
        res.append(ele > thresh)
    return res


# mesma coisa, ainda mais inteligente...
def elementwise_greater_than3(L, thresh):
    return [ele > thresh for ele in L]


def menu_is_boring(meals):
    """Given a list of meals served over some period of time, return True if the
    same meal has ever been served two days in a row, and False otherwise.
    """
    length = len(meals)
    for i in range(length-1):
        if meals[i] == meals[i+1]:
            return True
    return False
