# Um script que leia um valor em metros e o exiba convertido em centimetros e milimetros.

v1=float(input('Quantos metros? '))

c1 = v1 * 100
m1 = v1 * 1000

print('{} centimentros, {} milimetros'.format(c1,m1))
