# Um script que converta uma temperatura digitada em °C e converta para °F.

t1=int(input('Escreva a temperatura em °C: '))

t2=int(t1*(9/5)+32)

print('{}°C são {}°F.'.format(t1,t2))