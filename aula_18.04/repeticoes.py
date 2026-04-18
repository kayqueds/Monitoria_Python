'''
for (para) -> tem um limite 
while (enquanto) -> tem um 
'''
'''

repetição partes
1 - contador
2 - condição
3 - incremento + -



#exemplo 1
for i in range(200):
    print('Hello World')


num = int(input('Digite um número: '))

while num >= 0:
    print(num)
    num = num - 1
'''

print('---Tabuada----')
num = int(input('Digite um número: '))

if num >= 1 and num <= 10:
    print(f'Tabuada de {num}: ')
    for contador in range(1,11):
        vezes = num * contador
        print(f'{num} x {contador} = {vezes}')
else:
    print('Número inválido, deve ser entre 1 e 10')           






'''
    eu quero que você diga se a media for maior 6
    aprovado
    senao
    reprovado 
'''



n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
n3 = float(input('Digite a nota 3: '))


media = (n1+n2+n3)/3


print(f'A sua média foi: {media:.2f}')
# comparação
if media >= 6 and media <= 10:
    print('Aprovado')
elif media >= 3:
    print('Recuperação')
else:
    print('Reprovado')        
