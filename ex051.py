n1 = int(input('primeiro termo: '))
r = int(input('razão: '))
d = n1 + (10 - 1) * r
for c in range(n1, d + r, r):
    print(c, end=' ')
