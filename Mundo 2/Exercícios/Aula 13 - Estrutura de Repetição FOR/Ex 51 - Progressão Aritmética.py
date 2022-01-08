a1 = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

for contagem in range(1, 11):
    an = a1 + (contagem - 1) * razao
    print(an, end=' ⇒ ' if contagem != 10 else ' ')

an = a1
print(a1, end=' ⇒ ')
for ciclos in range(1, 11):
    an = an + razao
    print(an, end=' ⇒ ' if ciclos != 10 else ' ')
