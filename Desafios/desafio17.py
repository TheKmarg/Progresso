import math as m
print('Digite os valores para calcular a hipotenusa de um triângulo retângulo!')
ca = int(input('Digite o tamanho do Cateto Adjacente: '))
co = int(input('Digite o tamanho do Cateto Oposto: '))
hip = float(m.sqrt(m.pow(ca, 2) + m.pow(co, 2)))

print('A hipotenusa de um triângulo retângulo com medidas de {} e {} é {:.3f}' .format(ca, co, hip))
