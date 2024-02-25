a1 = float(input('Digite uma distancia em metros: '))

print('A medida {:.1f} equivale à \n{:.3f}km \n{:.2f}hm \n{:.1f}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm'
      .format(a1, a1 / 1000, a1 / 100, a1 / 10, a1 * 10, a1 * 100, a1 * 1000))
