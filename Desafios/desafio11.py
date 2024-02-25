print('Informe os valores a seguir para saber quantos litros de tinta será necessário para pintar a parede!')
at = float(input('Qual a altura da parede? \n: '))
lg = float(input('Qual a largura da parede? \n: '))
a = at * lg

print('Uma parede contendo {}m de altura, e {}m de largura, possuí {}m²' .format(at, lg, a))
print('Será necessário {}L de tinta para pintar uma parede com {}m²' .format(a / 2, a))
