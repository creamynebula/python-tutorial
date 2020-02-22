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
