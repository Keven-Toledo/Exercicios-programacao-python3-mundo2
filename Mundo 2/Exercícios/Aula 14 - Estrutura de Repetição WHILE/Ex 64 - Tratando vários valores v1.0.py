print('O número 999 irá encerrar o looping de perguntas.')
contador = soma = 0
numeros = int(input('Digite um número: '))
while numeros != 999:
    soma += numeros
    contador += 1
    numeros = int(input('Digite um número: '))
print(f'''Você digitou {contador} números e 
a soma entre eles foi {soma}.''')
