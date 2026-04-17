'''
    Faça um programa que lei um número inteiro
    e imprima o dobro desse número
'''

numero = int(input('Digite um número inteiro: '))
dobro = numero * 2
print(f'O dobro de {numero} é {dobro}')



''''
    Faça um programa que peça dois nomes
    se for igual imprima "Nomes iguais"
    se for diferente imprima "Nomes diferentes"
'''

# decisão
nome1 = input('Digite o primeiro nome: ')
nome2 = input('Digite o segundo nome: ')
if nome1 == nome2:
    print('Nomes iguais')
else:    
    print('Nomes diferentes')  