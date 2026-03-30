lista = []
impar = list()
par = []
num = 'x'
resposta = ''
while True:
    num = int(input(f'Digite o {len(lista) + 1}º valor: '))
    lista.append(num)
    if num % 2 == '0':
        par.append(num)
    else:
        impar.append(num)
    while resposta not in 'NS':
        respota = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if resposta == 'N':
        break

print('-'*30)
print(f'os valores digitados foram {lista}')
print(f'os valores pares foram {par}')
print(f'os valores impares foram {impar}')