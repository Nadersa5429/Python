print('-'*40)
print('leitor de valores')
print('-'*40)
escolha = produtobaratonome = 'a'
nome = preco = total = preco1000 = produtobaratovalor  = count = 0
while True:
    nome = (input('Nome do produto: '))
    preco = int(input('Valor do produto: R$ '))
    total += preco
    count += 1
    if count == 0 or preco < produtobaratovalor:
        produtobaratovalor = preco
        produtobaratonome = nome
    if preco > 1000:
        preco1000 += 1
    while not escolha in 'SN':
        escolha = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if escolha == 'N':
        break
print('-'*40)
print(f'''Total da compra foi R$ {total:.2f}
Total de produtos custam mais que R$1000: {preco1000}
O nome do produto com menor preço é {produtobaratonome}, e seu valor total é de {produtobaratovalor:.2f}''')

