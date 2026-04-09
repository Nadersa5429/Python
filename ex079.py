numeros = list()
while True:
    n = input('informe um valor: ')
    if n not in numeros:
        numeros.append(n)
        print('adicionado com sucesso')
    else:
        print('O número já está na lista, não foi adicionado')
    r = input('Você quer continuar? [S/N] ').strip().upper()[0]
    if r in ('Nn'):
        (numeros).sort()
        print(f'a lista em ordem crescente é: {numeros}')
        print('programa encerrado...')
        break