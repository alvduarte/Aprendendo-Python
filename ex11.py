# Um script que leia quanto dinheiro a pessoa tem na carteira 
# e mostre quantos dolares ela pode comprar. Considere US$1,00 = R$5,68

r1 = float(input('Quantos você tem em reais? '))
d1 = r1 / 5.68

print('Seu {} reais, valem {} dolares'.format(r1,d1))
