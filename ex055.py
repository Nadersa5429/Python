maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('digite o peso da {}ª pessoa: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            peso = menor
print('o maior peso lido foi {}'.format(maior))
print('o menor peso lido foi {}'.format(menor))

