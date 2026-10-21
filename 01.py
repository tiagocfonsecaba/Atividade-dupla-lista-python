import os

os.system('cls')

vetor = []
for i in range(5):
    numero = int(input(f'Numero {i+1}: '))
    vetor.append(numero)

print("\n Ordem digitada: ", vetor)


print("\n Ordem contraria: ", vetor[::-1])