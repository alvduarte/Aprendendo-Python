# Um script que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada.

dia = input('que dia você nasceu?')
mes = input('de que mês?')
ano = int(input('de qual ano?'))


idade = 2025 - ano  # extra xd

print('você nasceu em ', dia, '/', mes, '/',
      ano, ' e está com ', idade, ' anos')
