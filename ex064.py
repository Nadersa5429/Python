escolha = 0
soma = 0
repeat = 0
print('Digite um número pra adicionar a soma[digite 999 para parar]')
while escolha != 999:
    escolha = int(input(''))
    if escolha != 999:
        soma += escolha
        repeat += 1
print('Foram somados {} números e o resultado foi {}'.format(repeat,soma))
