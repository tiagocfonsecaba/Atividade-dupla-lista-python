import os
os.system('cls')

numeros = []
soma = 0
maior_10 = 0

for i in range(10):
    numero = int(input(f'digite um numero inteiro {i+1}° '))
    
    numeros.append(numero)

    for numero in numeros:
        soma += numero
        if numero > 10 :
            maior_10 += 1
            
    print(f'\n soma de todos os numeros inteiros: {soma}')
    print(f'\n soma de numeros maiores que 10: {maior_10}')