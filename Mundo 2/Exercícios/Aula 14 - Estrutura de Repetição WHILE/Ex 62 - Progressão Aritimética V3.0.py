primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
mais = 10
total = 0
contador = 1
while mais != 0:
    total += mais
    while contador <= total:
        print(f'{termo} - ', end='')
        termo += razao
        contador += 1
    print('Pausa')
    mais = int(input('Deseja ver mais quantos termos? '))

print(f'Foram lidos {contador} termos')
