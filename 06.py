import os
os.system ('cls')


vetor_A = []
vetor_B = []
vetor_C = []


print("Digite 5 números inteiros para o vetor A:")
for i in range(5):
    num = int(input(f"Vetor A [{i}]: "))
    vetor_A.append(num)

print("\nDigite 5 números inteiros para o vetor B:")

for i in range(5):
    num = int(input(f"Vetor B [{i}]: "))
    vetor_B.append(num)


for i in range(5):
    soma = vetor_A[i] + vetor_B[i]
    vetor_C.append(soma)


print("\n--- Resultados ---")
print(f"Vetor A: {vetor_A}")
print(f"Vetor B: {vetor_B}")
print(f"Vetor C (A + B): {vetor_C}")
