from datetime import date
nome = str(input('Seu nome: ')).strip().capitalize()
sexo = str(input('Sexo [M/F]: '))
nascimento = int(input('Ano de Nascimento: '))
ano_atual = date.today().year

idade = ano_atual - nascimento

alistamento = 18
menor_idade = alistamento - idade
maior_idade = idade - alistamento
tempo_restante = menor_idade + ano_atual
tempo_passado = ano_atual - maior_idade

if sexo in 'Mm':
    print(f'Quem nasceu em {nascimento} completará {idade} anos em {ano_atual}')
    if idade < alistamento:
        print(f'Ainda faltam {menor_idade} anos para o alistamento')
        print(f'Seu alistamento será em {tempo_restante}.')
    elif idade == alistamento:
        print(f'''Você tem {idade} anos e seu alistamento é nesse ano. 
Consulte o site do exército. ''')
    elif idade > alistamento:
        print(f'''Seu alistamento obrigatório foi em {tempo_passado}, 
{ano_atual - tempo_passado} anos atrás''')
else:
    print('Mulheres não são obrigadas por lei a se alistar.')
