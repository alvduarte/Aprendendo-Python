# Um script que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele

n = input('Digite algo:')

print('O tipo primitivo é', type(n))
print('É alfabético?', n.isalpha())
print('É alfanúmerico?', n.isalnum())
print('Só tem espaços?', n.isspace())
print('É um número?', n.isnumeric())
print('Está em maiúsculas?', n.isupper)
print('Está em minusculas?', n.islower())
print('Está capitalizada?', n.istitle())
