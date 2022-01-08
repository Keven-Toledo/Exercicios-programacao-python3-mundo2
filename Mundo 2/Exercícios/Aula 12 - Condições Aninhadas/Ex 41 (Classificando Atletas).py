from datetime import date
nome = str(input('Nome completo do atleta: ')).title().strip()
nasc = int(input('Ano de Nascimento do Atleta: '))
anoatual = date.today().year
idade = anoatual - nasc

print(f'Nome Completo: {nome}')
print(f'Idade do atleta: {idade} anos')

if idade <= 9:
    categoria = 'MIRIM'
    print(f'Categoria: {categoria}')
elif idade <= 14:
    categoria = 'INFANTIL'
    print(f'Categoria: {categoria}')
elif idade <= 19:
    categoria = 'JÚNIOR'
    print(f'Categoria: {categoria}')
elif idade <= 25:
    categoria = 'SÊNIOR'
    print(f'Categoria: {categoria}')
elif idade > 25:
    categoria = 'MASTER'
    print(f'Categoria: {categoria}')
