# Um script que leia o preço de um produto e mostre o seu novo preço, com 5% de desconto.

p1 = float(input('Quanto vale o produto? '))

p2 = p1-(p1*0.05)

print('Com desconto fica {}.'.format(p2))
