from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('=' * 40)
    print('''Escolha abaixo a opção desejada:
    [ 1 ] Somar os valores
    [ 2 ] Multiplicar os valores
    [ 3 ] Saber o maior valor
    [ 4 ] Digitar novos números
    [ 5 ] Sair do programa''')
    sleep(0.3)
    opcao = int(input('Informe a opção: '))
    sleep(0.5)
    if opcao == 1:
        soma = n1 + n2
        print('{} + {} = {}'.format(n1, n2, soma))
    elif opcao == 2:
        mult = n1 * n2
        print('{} x {} = {}'.format(n1, n2, mult))
    elif opcao == 3:
        maior = n1
        if n1 < n2:
            maior = n2
        print('Entre {} e {} o maior é {}'.format(n1, n2, maior))
    elif opcao == 4:
        n1 = int(input('Primeiro novo valor: '))
        n2 = int(input('Segundo novo valor: '))
    elif opcao == 5:
        print('Finalizando programa! Aguarde...')
    else:
        print('Opção Invalid! Tente novamente.')
    sleep(0.5)
print('Programa finalizado!')
