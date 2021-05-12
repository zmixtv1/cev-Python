
from math import sin, cos , tan, radians

a1 = int(input('Digite um angulo:'))
seno = sin(radians(a1))
coseno = cos(radians(a1))
tangente = tan(radians(a1))

print('O Seno do agulo é: {:.2f}\nO Cosseno do ângulo é: {:.2f}\nA tangente do Angulo é: {:.2f}'.format(seno, coseno, tangente))
