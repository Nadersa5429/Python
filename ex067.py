count = 1
n = resultado = 0
while True:
    print('-' * 30)
    n = int(input('Qual tabuada você deseja ver?'))
    print('-' * 30)
    if n < 0:
            break
    while count <= 10:
            resultado = n * count
            print(f'{n} x {count} = {resultado}')
            count += 1
    count = 1
    resultado = 0
print('Programa finalizado, volte sempre')