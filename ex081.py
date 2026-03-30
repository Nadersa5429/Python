lista = []
while True:
    num = 'x'
    while num not in '0123456789':
        num = (str(input('Digite um valor: ')))
    lista.append(num)
    resposta = 'x'
    while resposta not in 'SN':
        resposta = (str(input('Quer continuar? [S/N] '))).strip().upper()[0]
    if resposta == 'N':
        break
lista.sort(reverse=True)
print('_'*30)
print(f'no total foram digitados {len(lista)} valores')
print(f'a lista em ordem decrescente é {lista}')
if '5' in lista:
    print('O valor 5 apareceu na lista')
else:
    print('O valor 5 não apareceu na lista')
