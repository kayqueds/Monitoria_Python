'''

# ex1
print('Alô Mundo')

# ex2
numero = int(input('Digite um número: '))
print(f'O número informado foi {numero}')


# ex3
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
soma = n1+n2 
print(soma)



nota1 = float(input('Qual foi a sua nota 1: '))
nota2 = float(input('Qual foi a sua nota 2: '))
nota3 = float(input('Qual foi a sua nota 3: '))
nota4 = float(input('Qual foi a sua nota 4: '))


media =  (nota1+nota2+nota3+nota4)/4
print(f'Sua média foi: {media}')

'''


# % resto da divisao

print('----Par ou Impar---')

valor = int(input('Insira um número: '))

print(valor)
if valor %2 == 0:
    print('é par')
else:
    print('é impar')            

