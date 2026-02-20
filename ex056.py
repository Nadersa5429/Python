m = 0
nm = 0
mm= 0
n = 0
i = 0
s = 0
am = 0
for p in range(1, 5):
    n = input('Digite o nome da {}ª pessoa: '.format(p))
    i = int(input('quantos anos a {}ª pessoa tem? '.format(p)))
    s = input('Qual o sexo da {}ª pessoa? M/F ').strip().upper()
    m += i
    if s == 'M' and i > am:
        nm = n
        am = i
    if s == 'F' and i <= 20:
        mm += 1
media = m / 4
print('''A Média das idades é {} 
o homem mais velho se chama {} e tem {} anos
e foram informadas {} mulheres com menos de 20 anos'''.format(media, nm, am, mm))
