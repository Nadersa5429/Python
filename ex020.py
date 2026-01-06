import random

n1=input('qual o primeiro nome? ')
n2=input('qual o segundo nome? ')
n3=input('qual o terceiro nome? ')
n4=input('qual o terceiro nome? ')
lista=[n1,n2,n3,n4]
ordem=random.sample(lista,4)
print (ordem)