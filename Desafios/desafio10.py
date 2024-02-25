rs = float(input('Digite quantos Reais (R$) você deseja converter para outras moedas? \nR$'))
us = float(rs / 5.00)
yu = float(rs * 1.44)
print('Com R${:.2f} você poderá obter: \nU${:.2f} \n元{:.2f}' .format(rs, us, yu))
