# Um script que leia a largura e a altura de uma parede em metros, calcule a sua área 
# e a quantidade de tinta necessária para pintá-la, 
# sabendo que a cada litro de tinta pinta uma área de 2 m².

l = float(input('Qual a largura da parede? '))
a = float(input('Qual a altura da parede? '))

area = a*l
qntd = area*2

print('Sua parede tem {} m². Você precisa de {} litros de tinta.'.format(area, qntd))