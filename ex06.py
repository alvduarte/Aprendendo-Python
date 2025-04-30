# Um script que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

n1 = int(input('Digite um número: '))
s = n1+1
a = n1-1
print('O sucessor de {} é {}.'.format(n1,s), end=(' '))
print('O antecessor de {} é {}.'.format(n1,a))