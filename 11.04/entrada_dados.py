# Entrada de dados

nome = 'Kayque'
print(f'Oi {nome}')

# usando input para receber dados do usuário
pessoa = input('Digite seu nome: ')
print(f'Olá {pessoa}, tudo bem?')

''''
Tipos de dados
    string '' ou ""
    int 0, 1, 2, 3, 4, 5
    float 0.0, 1.5, 3.14
    bool True ou False
'''
idade = 5
print(f'Tipo de dado: {type(idade)}')
altura = 1.75
print(f'Tipo de dado: {type(altura)}')

print('-----Soma de dois números-----')
n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
soma = n1 + n2
print(f'A soma de {n1} e {n2} é: {soma}')