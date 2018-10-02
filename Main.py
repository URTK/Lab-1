import math

a = int(input('Введите A'))

y = math.cos(a)+math.sin(a)+math.cos(3*a)+math.cos(3*a)
z = (2*(math.sqrt(2)))*(math.cos(a))*(math.sin((math.pi/4)+2*a))

print('X = ',y - z)
