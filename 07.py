import os 
os.system('cls')

vetor1 = []
vetor2= []

for i in range(10):
    numero = int(input(f'digite o {i + 1}º: '))
    vetor1.append(numero)
    if numero > 0 :
        vetor2.append(numero)
        
print('\nVetor original:', vetor1)
print('Vetor dos positivos:', vetor2)
print('Quantidade de elementos copiados:', len(vetor2))