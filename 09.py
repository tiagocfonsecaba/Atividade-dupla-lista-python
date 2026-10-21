import os
os.system('cls')
import time
vetor = []

for i in range(6):
    numero = int(input('Digite o numero: '))
    vetor.append(numero)

print('Vetor antes:', vetor)

if len(vetor) == 6:
    for i in range(6):
        if vetor[i] % 2 == 0:
            vetor[i] = 0
        else:
            vetor[i] = 1

    print('Vetor depois:', vetor)