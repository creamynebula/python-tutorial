print('\n')
for i in range(10,20,2): #intervalo [10,20), de 2 em 2, entao 10, 12,...,18
     print(i)
#range retorna um iterável, não uma lista


olaa = ['mary','had','a','little','lamb']
print('\n')
for i in range(len(olaa)):
    print(i, olaa[i])


olaa2 = [1,2,3,4,5]
print('\n')
print(sum(olaa2))

olaa3 = list(range(10,20,2)) #agora temos uma lista
print('\n')
print(olaa3)

print('\n')
for numero in range(2,10):
    for divisor in range(2,numero):
        if numero%divisor == 0:
            print (numero, 'não é primo, ele é igual a', int((numero/divisor)),'*',divisor)
            #quebra o for porque descobrimos que o numero nao é primo
            break
    else:
        #else só executado se um for/while acabar porque acabou de iterar(for) comparacao deu false(while)
        #nao é executado se o for/while acabar por causa de um break
        #em resumo, else de loop é executado se nao houver break
        #se chegamos aqui, é pq não achamos divisor pro numero, ele é primo
        print(numero,'é primo')

print('\n')
for x in range (11):
    if x%2 == 0:
        print(x,'é par')
        continue #pula pra próxima iteração
    print(x, 'é impar')

print('\n')
v1 = [1,2]
for i in range(10):
    v1.append(1)
    v1.append(2)
print(v1)

print('\n')
a = int(input('digite numero: '))
if a in v1:
    print (a,'está presente em',v1)