# Crie um script que leia um número real qualquer pelo teclado e mostre na tela a sua protção inteira
from math import trunc
num = float(input('Digite um número real: '))

truncado = trunc(num)

print('A parte inteira do número {} é {}'.format(num, truncado))
