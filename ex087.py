matriz = [[], [], []]
linha = coluna = 0
soma = maior = somacoluna = 0
for count in range (1, 10):
    if count == 0 or count == 4 or count == 7:
        coluna = 1
    else:
        coluna += 1
    if coluna == 1:
        linha += 1
    num = int(input(f'digite um valor para [{linha}|{coluna}]: '))
    if linha == 1:
        matriz[0].append(num)
    if linha == 2:
        matriz[1].append(num)
    if linha == 3:
        matriz[2].append(num)
    if num % 2 == 0:
        soma += num
    if coluna == 3:
        somacoluna += num
print('=-' * 30)
for linha in range (0, 3):
    for coluna in range (0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
print('=-'*30)
print(f'A soma dos valores pares da matriz é igual a {soma}')
print(f'A soma dos valores da terceira coluna é igual a {somacoluna}')
print(f'O maior valor da segunda linha é igual a {max(matriz[1])}')