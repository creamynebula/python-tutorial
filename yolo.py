print(r'C:\Chihaya\name') #yep, r = "raw string", entao \n e etc nao sao interpretados como special characters
print('\n')
#veja soh, com triple quotes as newlines sao adicionadas automaticamente, isso vai ser impresso tudo formatadinho
#a barra na 1a linha porém faz nao adicionar \n na 1a linha, então vai começar a imprimir a partir de 'Usage'
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""") 
s = 'supercalifragilisticexpialidocious'
print("tamanho da string s: ",len(s),'\n')

certoMagicoVetor = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]
certoMagicoVetor[2:5] = [4,3,2]
print(certoMagicoVetor)
certoMagicoVetor[2:5] = []
print(certoMagicoVetor,'\n')

#some fib
a,b = 0,1
while (a < 90):
     print(a)
     a,b=b,a+b

print('\n')
a,b = 0,1

while (a < 90):
     print(a, end=',') #normalmente
     a,b=b,a+b

print('\n')
a=int(input('Entra um número parça: '))
if a < 0:
     print('neg')
elif a > 0:
     print('not neg')
else:
     print('ZERO')

