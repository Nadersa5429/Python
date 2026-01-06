s=float(input('Qual o sálario do funcionario? R$'))
if s <=1250.00:
    a=s+(s*15/100)
else:
    a=s+(s*10/100)
print('Quem ganhava {:.2f} agora ganha {:.2f}'.format(s,a))

