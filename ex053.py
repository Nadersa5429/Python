f = input('digite uma palavra/frase: ').strip().upper()
p = f.split()
j = ''.join(p)
i = ''
for letra in range(len(j)-1, -1, -1):
    i += j[letra]
print('o inverso de {} é {}'.format(j,i))
if j == i:
    print('temos um palindromo')
else:
    print('não é um palindromo')
