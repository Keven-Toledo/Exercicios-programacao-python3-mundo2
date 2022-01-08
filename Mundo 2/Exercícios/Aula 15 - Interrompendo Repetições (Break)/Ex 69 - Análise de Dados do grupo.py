from time import sleep
generos = ('M', 'F')
sexo = ''
contador = contador_masc = contador_idade_femi = contador_idade = 0
while True:
    contador += 1
    print('=' * 25)
    print(f'Cadastro da {contador}ª pessoa')
    print('=' * 25)
    idade = int(input('Idade: '))
    if idade >= 18:
        contador_idade += 1
    sexo = str(input('Sexo: ')).strip().upper()[0]
    while sexo not in generos:
        sexo = str(input('Sexo: ')).strip().upper()[0]
    if sexo == 'M':
        contador_masc += 1
    if sexo == 'F':
        if idade < 20:
            contador_idade_femi += 1
    print('_' * 25)
    opcao = str(input('Deseja continuar? ')).strip().upper()[0]
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar? ')).strip().upper()[0]
    if opcao == 'N':
        break

print('=' * 25)
print('Analisando...')
print('=' * 25)
sleep(1.5)
if contador_masc and contador_idade_femi and contador_idade > 0:
    print(f'''Cadastros: {contador}
Homens cadastrados: {contador_masc}
Maiores de 18 anos: {contador_idade}
Mulheres com menos de 20 anos: {contador_idade_femi} ''')
elif contador_masc == 0:
    print(f'''Cadastros: {contador}
Não houveram homens cadastrados
Maiores de 18 anos: {contador_idade}
Mulheres com menos de 20 anos: {contador_idade_femi} ''')
elif contador_idade == 0:
    print(f'''Cadastros: {contador}
Homens cadastrados: {contador_masc}
Não houveram maiores de 18 anos
Mulheres com menos de 20 anos: {contador_idade_femi} ''')
elif contador_idade_femi == 0:
    print(f'''Cadastros: {contador}
Homens cadastrados: {contador_masc}
Maiores de 18 anos: {contador_idade}
Não houveram mulheres menores de 20 anos''')
