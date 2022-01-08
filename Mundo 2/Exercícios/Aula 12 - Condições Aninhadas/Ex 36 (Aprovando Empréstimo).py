valor_casa = float(input('Digite o preço da casa:  R$ '))
salario_liquido = float(input('Digite seu salário liquido: R$ '))
anos = int(input('Em quantos anos pretende pagar: '))
meses = anos * 12
limite = salario_liquido * 0.3
mensalidade = valor_casa / meses

if mensalidade <= limite:
    print('-' * 29)
    print('Valor da casa: R${:.0f}'.format(valor_casa))
    print('Seu salário: R${:.0f}'.format(salario_liquido))
    print('Tempo: {} anos'.format(anos))
    print('Prestação: {} mensal'.format(mensalidade))
    print('Limite: {}'.format(limite))
    print('-' * 29)
    print('Empréstimo: \033[32m APROVADO!')
else:
    print('-' * 29)
    print('Valor da casa: R${:.0f}'.format(valor_casa))
    print('Seu salário: R${:.0f}'.format(salario_liquido))
    print('Tempo: {} anos'.format(anos))
    print('Prestação: {} mensal'.format(mensalidade))
    print('Limite: {}'.format(limite))
    print('-' * 29)
    print('Empréstimo: \033[31m NEGADO!')
