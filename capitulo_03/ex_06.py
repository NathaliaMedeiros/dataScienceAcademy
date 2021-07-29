"""
Crie uma variável chamada contador = 0. Enquanto counter for menor que 100, imprima os valores na tela,
 mas quando for encontrado o valor 23, interrompa a execução do programa
"""

counter = 0

while counter < 100:
    if counter == 23:
        break
    else:
        print(counter)
        counter += 1

