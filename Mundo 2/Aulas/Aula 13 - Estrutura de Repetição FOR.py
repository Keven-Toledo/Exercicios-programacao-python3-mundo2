"""s = 0
for c in range(0, 4):
    n = int(input('Digite um número: '))
    s = s + n
print('O somatorio foi {}'.format(s))"""

"""for c in range(6, 0, -1):
    print(c)
print('FIM')"""

"""for contagem in range(0, 7, 2):
    print(contagem)
print('FIM')"""

"""n = int(input('Digite um número: '))
for contagem in range(0, n+1):
    print(contagem)
print('FIM')"""

"""i = int(input('Início: '))
f = int(input('Final: '))
p = int(input('Passo: '))
for contagem in range(i, f+1, p):
    print(contagem)
print('FIM')"""

"""for contagem in range(0, 5):
    n = int(input('Digite um valor: '))
print('Fim')"""

"""soma = 0
for somatorio in range(0, 4):
    n = int(input('Digite um número: '))
    soma = soma + n
    print(soma)
print('O somatório de todos os valores foi {}'.format(soma))"""
# O laço mostra cada objeto que está em cda indíce dentro da lista
"""frutas = ['Abacaxi', 'Morango', 'Uva']
for fruta in frutas:
    print(fruta)"""

"""for fruta in ['Abacaxi', 'Morango', 'Uva']:
    print(fruta)"""

# Repetindo os caracteres de uma string
"""palavra = 'Vamos estudar Python'
for letra in palavra:
    print(letra)"""

#Parar um loop antes dele terminar
"""pessoas = [({'nome': 'João', 'Cidade': 'Belo Horizonte'}),
           ({'nome': 'Maria', 'Cidade': 'São Paulo'}),
           ({'nome': 'Pedro', 'Cidade': 'Curitiba'})]
contador = 0
for pessoa in pessoas:
    contador += 1
    print(contador)
    if pessoa['nome'] == 'Maria':
        print(pessoa['nome'], 'mora em', pessoa['Cidade'])
        break"""
# Interrompendo o loop e continuando no róximo objeto: continue
"""pessoas = [({'nome': 'João', 'Cidade': 'Belo Horizonte'}),
           ({'nome': 'Maria', 'Cidade': 'São Paulo'}),
           ({'nome': 'Pedro', 'Cidade': 'Curitiba'})]
contador = 0
for pessoa in pessoas:
    contador += 1
    if pessoa['nome'] == 'Maria':
        continue
    print(contador)
    print(pessoa['nome'], 'mora em', pessoa['Cidade'])"""
# Retornando uma sequência de números: range()
"""for numeros in range(1, 5, 2):
    print(numeros)"""
"""for numero in range(11):
    if numero % 2 == 0:
        print('O número {} é par'.format(numero))"""
"""for numero in range(10, 21):
    if numero % 2 == 0:
        print('O número {} é par'.format(numero))"""
#Executando um código quando o loop chega ao fim: else no loop for.
"""frutas = ['Abacaxi', 'Maça', 'Morango', 'Uva',]
for fruta in frutas:
    print(fruta)
else:
    print('Laço de repetição finalizado sem pausas')"""
# Laços aninhados
"""for numero_coluna1 in range(2, 5):
    print('Tabuada do', numero_coluna1)
    for numero_coluna2 in range(11):
        print(numero_coluna1, 'x', numero_coluna2, '=', numero_coluna1 * numero_coluna2)"""
# Como executar um loop sem conteúdo: pass
for numero in range(10):
    pass


