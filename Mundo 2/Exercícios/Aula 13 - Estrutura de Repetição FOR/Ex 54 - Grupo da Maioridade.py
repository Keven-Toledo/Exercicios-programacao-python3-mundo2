from datetime import date
cont_maior_idade = cont_menor_idade = cont_total = 0

for ciclo in range(1, 8):
    nascimento = int(input(f'Ano de nascimento da {ciclo}ª pessoa: '))
    ano_atual = date.today().year
    idade = ano_atual - nascimento
    cont_total += 1
    if idade >= 18:
        cont_maior_idade += 1
    else:
        cont_menor_idade += 1
print(f'''{cont_total} pessoas contabilizadas; 
{cont_maior_idade} são maiores de idade;
{cont_menor_idade} são menores de idade.''')
