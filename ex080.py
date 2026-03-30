num = []
for c in range(0,5):
    n = int(input(f'Digite o {c+1}º valor: '))
    if c == 0 or n > num[len(num)-1]:
        num.append(n)
    else:
        pos = 0
        while pos < len(num):
            if n < num[pos]:
                num.insert(pos, n)
                break
            pos += 1
print('_'*30)
print(f'os valores digitados organizados em ordem crescente foram {num}')





