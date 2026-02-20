escolha = 'S'
n = menor = maior = acumulador = soma = 0
while escolha == 'S':
    n += int(input('Digite um número: '))
    acumulador += 1
    soma += n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    escolha = str(input('Quer continuar? [S/N] ')).strip().upper()
media = soma / acumulador
print('Foram digitados {} números e a média encontrada foi {}, o maior número foi {} e o menor foi {}'.format(acumulador, media, maior, menor ))
