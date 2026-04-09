numeros = []
maior = menor = 0
for c in range(0, 5):
    numeros.append(input(f'Digite um valor para ficar na posição {c+1}: '))
    if c == 0:
        maior = menor = numeros[c]
    elif numeros[c] > maior:
        maior = numeros[c]
    elif numeros[c] < menor:
        menor = numeros[c]
print(f'Você digitou os valores {numeros}')
print(f'O maior número informado foi {maior} nas posições ', end='')
for i, v in enumerate(numeros):
    if v == maior:
        print(f'{i+1}...', end='')
print()
print(f'O menor número informado foi {menor} nas posiçes ', end='')
for i, v in enumerate(numeros):
    if v == menor:
        print(f'{i+1}...', end='')