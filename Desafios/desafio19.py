import random as r
print('Digite 4 nomes para serem sorteados: ')
n1 = str(input())
n2 = str(input())
n3 = str(input())
n4 = str(input())
nomes = [n1, n2, n3, n4]

print('Este foi o nome escolhido: {}!'.format(r.choice(nomes)))
