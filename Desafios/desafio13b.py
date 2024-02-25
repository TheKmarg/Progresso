prec = float(input('Digite o preço do produto. \nR$'))
dsc = prec - (prec * 0.10)
jr = prec + (prec * 0.08)

print('O produto que custa R${:.2f}.' .format(prec))
print('A vista o produto ficará por R${:.2f}, e se for parcelado ficará no total por R${:.2f}' .format(dsc, jr))
