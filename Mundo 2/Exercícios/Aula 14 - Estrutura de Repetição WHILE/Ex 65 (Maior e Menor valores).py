resposta = 'S'
soma = contador = media = maior = menor = 0
while resposta in 'S':
    numero = int(input('\033[34mDigite um número: \033[m'))
    soma += numero
    contador += 1
    if contador == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero
    resposta = str(input('\033[33mQuer continuar [S/N]? \033[m')).strip().upper()[0]
media = soma / contador
print(f'você digitou {contador} números e a sua média foi de {media}')
print(f'O maior número foi {maior} e o menor foi {menor}.')
