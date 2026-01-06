p = float(input('Digite o valor do produto: '))
d = p - 10/100
ca = p - 5/100
c2 = p
c3 = p + 20/100
e = 5
o = int(input('informe a opção desejada: \n 1_Dinheiro ou cheque \n 2_Cartão a vista \n 3_Cartão de 2x \n 4_Cartâo de 3x ou mais \n 5_sair \n'))
if o == 1:
    print(d)
elif o == 2:
    print(ca)
elif o == 3:
    print(c2)
elif o == 4:
    print(c3)
else:
    print('Uma pena que não vá comprar, volte sempre')