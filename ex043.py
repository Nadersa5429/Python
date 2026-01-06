p = float(input('Qual o seu peso?'))
a = float(input('Qual a altura?'))
imc = p / (a * a)
if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc <= 25:
    print('Peso ideal')
elif imc >= 25 and imc <= 30:
    print('Sobrepeso')
elif imc >= 30 and imc <= 40:
    print('Obesidade')
else:
    print('obesidade mórbida')