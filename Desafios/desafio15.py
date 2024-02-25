print('Informe as informações pedidas após o uso do carro alugado.')
d = int(input('Quantos dias foi utilizado o carro? '))
km = float(input('Quantos KM foram rodados com o carro? '))
vd = d*60
vkm = km*0.15

print('O valor pelo uso de dias foi: R${:.2f}' .format(vd))
print('E o valor pelos KM rodados foi: R${:.2f}' .format(vkm))
print('O total foi de: R${:.2f}' .format(vd + vkm))
