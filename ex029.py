v=int(input('qual sua velocidade?'))
if v > 80:
    print ('voce foi multado')
    multa = (v-80)*7
    print ('o valor da multa é {}'.format(multa))
else:
    print ('tenha um bom dia!')