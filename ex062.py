print('Gerador de PA')
print('-='*10)

n1 = int(input('primeiro termo: '))
r = int(input('razão: '))
termo = n1
count = 0
faltando = 10
while faltando != 0:
    while faltando > 0:
        print('{} ->'.format(termo), end='')
        termo += r
        count += 1
        faltando -= 1
    print(' PAUSA')
    faltando = int(input('Mais quantos termos você deseja ver? '))
print('A PA foi finalizada mostrando um total de {} termos'.format(count))