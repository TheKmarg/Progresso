import math as m
an = float(input('Digite um ângulo: '))

print('O sen, cos e tan do ângulo {} são:' .format(an))
print('Seno: {:.2f}' .format(m.sin(m.radians(an))))
print('Cosseno: {:.2f}' .format(m.cos(m.radians(an))))
print('Tangente: {:.2f}' .format(m.tan(m.radians(an))))
