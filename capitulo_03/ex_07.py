"""
Crie uma lista vazia e uma variável com valor 4. Enquanto o valor da variável for menor ou igual a 20,
adicione à lista, apenas os valores pares e imprima a lista
"""

lst = []

x = 4

while x <= 20:
    if x % 2 == 0:
        lst.append(x)
        x += 1
    else:
        x += 1

print(lst)

