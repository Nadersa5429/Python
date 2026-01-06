d=int(input('qual a distancia da viagem: '))
if d <=200:
    v=d*0.50
else:
    v=d*0.45
print('sua viagem vai custar {}'.format(v))