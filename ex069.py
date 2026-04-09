idade = sexo = maior = homem = mulher20 = escolha = total = 0
print('-'*50, )
print('Sistema de cadastro, seja bem vindo')
print('-'*50)
while True:
    while sexo not in 'MF':
        sexo = input('Digite o sexo  do usuário (M/F): ').strip().upper()[0]
    idade = int(input('Digite a idade do usuário: '))
    if sexo == 'M':
        homem += 1
    elif idade > 18:
        maior += 1
    elif idade < 20 and sexo == 'F':
        mulher20 += 1
    total += 1
    while escolha not in 'NS':
        escolha = input('Quer continuar? [S/N]: ').strip().upper()[0]
    if escolha == 'N':
        break
print(f'''Total de pessoas com mais de 18 anos: {maior}
Total de homens cadastrados: {homem}
Total de mulheres com menos de 20 anos: {mulher20}
Total de pessoas cadastradas: {total}''')