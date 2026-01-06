from datetime import date
i = int(input('Digite o ano de nascimento: '))
atual = date.today().year
if atual - i <=9:
    print('mirim')
elif atual - i <=14:
    print('infantil')
elif atual - i <=19:
    print('junior')
elif atual - i <=20:
    print('sênior')
else:
    print('master')

