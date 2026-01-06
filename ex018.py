import math
a=float(input('qual ângulo você deseja? '))
s=math.sin(math.radians(a))
c=math.cos(math.radians(a))
t=math.tan(math.radians(a))
print ('o seno de {} é {:.2f}'.format(a,s))
print ('o cos de {} é {:.2f}'.format(a,c))
print ('a tan de{} é {:.2f}'.format(a,t))
