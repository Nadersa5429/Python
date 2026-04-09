matriz = [[], [], []]
linha = coluna = 0
for c in range (1, 10):
    if c == 0 or c == 4 or c == 7:
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
print('=-' * 30)
print(f'''{matriz[0]}
{matriz[1]}
{matriz[2]}''')