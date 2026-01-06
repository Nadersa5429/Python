n = int(input('informe um número'))
b = bin(n)
o = oct(n)
h = hex(n)
e = 0
while e < 4:
    e = int(input('escolha sua opção \n 1_binario \n 2_octal \n 3_hexadecimal \n 4_sair \n'))

    if e == 1:
     print(b[2:])
    elif e == 2:
     print(o[2:])
    elif e == 3:
        print(h[2:])