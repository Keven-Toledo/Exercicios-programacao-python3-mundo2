maior = menor = 0

for ciclo in range(1, 6):
    peso = float(input(f'Digite o peso da {ciclo}ª pessoa: '))
    if ciclo == 1:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print(f'O maior peso lido foi {maior}Kg.')
print(f'O menor peso lido foi {menor}Kg.')
