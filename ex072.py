numero = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
          'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
          'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
          'dezesete', 'dezoito', 'dezenove', 'vinte')
opcao = int(input('digite um número de 0 a 20: '))
while True:
    if 0 <= opcao <= 20:
        print('você digitou o número', numero[opcao])
        escolha = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
        if escolha in 'Nn':
            break
        elif escolha in 'Ss':
            opcao = int(input('digite um número de 0 a 20: '))
    else:
        print('Tente novamente.', end='')
