n1=float(input('informe a primeira nota'))
n2=float(input('informe a segunda nota'))
m = (n1 + n2)/2
if m < 5:
    print('reprovado')
elif m >= 5 and m <= 6.9:
    print('recuperação')
else:
    print('aprovado')