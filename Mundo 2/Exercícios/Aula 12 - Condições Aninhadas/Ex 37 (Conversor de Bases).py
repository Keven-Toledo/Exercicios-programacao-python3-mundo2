num = int(input('Digite um Valor inteiro:'))
print('=' * 40)
print('''Digite o número da base desejada: 
[ 1 ] Converter para Binário
[ 2 ] Converter para Octal
[ 3 ] Converter para Hexadecimal''')
opcao = str(input('Digite o número: '))
print('=' * 40)

if opcao == '1':
    print('O número {} convertido para binário é: {}'.format(num, bin(num)[2:]))
elif opcao == '2':
    print('O número {} convertido para octal é: {}'.format(num, oct(num)[2:]))
elif opcao == '3':
    print('O número {} convertido para Hexadecimal é: {}'.format(num, hex(num)[2:]))
else:
    print('\033[31m''Número inválido!')
