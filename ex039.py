from datetime import date
a = date.today().year
n = int(input('Em qual ano você nasceu? '))
al = n + 18
p = a - al
m = al - a
if a - n == 18:
    print('você tem que se alistar esse ano')
elif a - n > 18:
    print('já se passaram {} anos da data que você deveria se alistar'.format(p))
else:
    print('ainda faltam {} anos para o alistamento'.format(m))
