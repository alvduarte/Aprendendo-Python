# Um scrip que leia o salário de um funcionário e mostre seu novo sálario, com 15% de aumento.

s1 = float(input('Qual o salário do funcionário? '))
s2 = s1 + s1*0.15

print('O salário com aumento ficará {:.2f}.'.format(s2))