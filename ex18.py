# Faça um scrip que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa

import math

catoposto = int(input('Digite um cateto: '))
catadja = int(input('Digite outro cateto: '))

hipotenusa = math.sqrt(catoposto**2 + catadja**2)

print('A hipotenusa é ', hipotenusa)
