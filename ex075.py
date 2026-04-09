
tupla = (int(input('Digite um valor: ')),
         int(input('Digite um valor: ')),
         int(input('Digite um valor: ')),
         int(input('Digite um valor: ')))
print(f'Você digitou os números {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O valor 3 foi digitado pela primeira vez na {tupla.index(3)+1}ª posição')
else:
    print('O valor 3 não foi informado')
print('Os valores pares digitados foram : ',end='')
for c in tupla:
    if c % 2 == 0:
        print(c, end=',')