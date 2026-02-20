n = int(input('digite um numero '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[34m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('o número {} foi dividido {} vezes'.format(n, tot))
if tot == 2:
    print('por isso ele é primo')
else:
    print('por isso não é primo')