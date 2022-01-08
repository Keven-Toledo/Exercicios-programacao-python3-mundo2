produto = float(input('Preço do produto: R$'))
print('''Forma de pagamento: 
[ 1 ] à vista no dinheiro (-10%)
[ 2 ] à vista no cartão (-5%)
[ 3 ] 2x no cartão (Preço normal)
[ 4 ] 3x ou mais no cartão (+20%)''')
opcao = str(input('Opção desejada: '))

if opcao == '1':
    pagamento = produto * 0.9
    print('O preço passa de R${:.2f} para R${:.2f}'.format(produto, pagamento))
elif opcao == '2':
    pagamento = produto * 0.95
    print('O preço passa de R${:.2f} para R${:.2f}'.format(produto, pagamento))
elif opcao == '3':
    pagamento = produto
    print('O preço de R${:.2f} se mantém.'.format(pagamento))
elif opcao == '4':
    pagamento = produto * 1.2
    parcelas = int(input('Quantas parcelas? '))
    fatura = pagamento / parcelas
    print('''Sua compra será parcelada em {}x de {.2f'}. 
O preço passa de R${:.2f} para R${:.2f}'''.format(parcelas, fatura, produto, pagamento))
else:
    print('\033[1;31;40m''OPÇÃO INVÁLIDA''\033[m')
