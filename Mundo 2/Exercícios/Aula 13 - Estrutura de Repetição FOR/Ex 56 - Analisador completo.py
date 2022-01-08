soma_idades = cont_ciclos = cont_masc = 0
cont_femi = maior_idade_M = menor_idade_F = 0
nome_mais_velho = ''

for ciclo in range(1, 5):
    print(f'-----{ciclo}ª PESSOA-----')
    nome = str(input('Nome: ')).title().strip()
    idade = int(input('idade: '))
    sexo = str(input('Sexo [M/F]: ')).title().strip()[0]
    cont_ciclos += 1
    soma_idades += idade
    if sexo in 'Mn':
        cont_masc += 1
        if cont_masc == 1:
            maior_idade_M = idade
            nome_mais_velho = nome
        else:
            if idade > maior_idade_M:
                maior_idade_M = idade
                nome_mais_velho = nome
    elif sexo in 'Ff':
        cont_femi += 1
        if idade < 20:
            menor_idade_F += 1

media_idades = soma_idades / cont_ciclos
print(f'A média das idades vale: {media_idades} anos.')

if cont_masc != 0:
    print(f'Homem mais velho: {nome_mais_velho}, {maior_idade_M} anos')
else:
    print('Não houveram homens na pesquisa')

if cont_femi != 0:
    if cont_femi == 1:
        print(f'Há {cont_femi} mulher na pesquisa, com', end=' ')
        if menor_idade_F == 1:
            print('menos de 20 anos')
        elif menor_idade_F == 0:
            print('mais de 20 anos')
    elif cont_femi != 1:
        print(f'Há {cont_femi} mulheres na pesquisa,', end=' ')
        if menor_idade_F > 1:
            print(f'{menor_idade_F} com menos de 20 anos')
        elif menor_idade_F == 0:
            print(f'mas nenhuma com menos de 20 anos')
else:
    print('Não houveram mulheres na pesquisa')
