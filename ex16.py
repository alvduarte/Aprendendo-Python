# Um script que pergunte a quantidade de Km percorridos por um carro alugado 
# e a quantidade de dias pelos quais ele foi alugado. 
# Calcule o preço a pagar, sabendo que o carro custa R$60por dia e R$0,15 por km rodado.

km = float(input('Quantos km rodou? '))
dias = int(input('Quantos dias pegou? '))

total=int(dias*60+km*0.15)

print('Você deve pagar R${}.'.format(total))

