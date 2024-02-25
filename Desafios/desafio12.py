vl = float(input('Digite o preço do produto! \nR$'))
dsc = vl - (vl * 0.05)

print('Você recebeu 5% de desconto, o produto de R${} agora é de R${:.2f}' .format(vl, dsc))
