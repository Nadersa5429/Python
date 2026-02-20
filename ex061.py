print('Gerador de PA')
print('-='*10)

n1 = int(input('primeiro termo: '))
r = int(input('razão: '))
termo = n1
count = 1
while count <= 10:
    print('{}'.format(termo), end=' -> ')
    termo += r
    count += 1
print('\n FIM')