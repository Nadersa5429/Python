f=str(input('Digite uma frase: ')).strip().lower()
print ('A letra "A" aparece {} vezes'.format(f.count('a')))
print ('A letra "A" aparece pela primeira vez {} '.format(f.find('a')+1))
print ('A ultima letra "A" aparece {} vezes'.format(f.rfind('a')+1))

