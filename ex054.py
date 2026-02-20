from datetime import date
a = date.today().year
m = 0
me = 0
for c in range(1, 8):
    n = int(input('quando a {}º pessoa nasceu? '.format(c)))
    i = a - n
    if i >= 21:
        m += 1
    else:
        me += 1
print('{} pessoas são maiores e {} são menores'.format(m,me))