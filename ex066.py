count = 0
soma = 0
n = 0
while True:
    n = int(input('digite um número: '))
    if n == 999:
        break
    else:

        soma += n
        count += 1
print(f'foram digitados {count} números ea soma deles é igual a {soma}')