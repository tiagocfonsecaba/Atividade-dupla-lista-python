import os
os.system

print("Inserindo numeros:")

vetor = []

# Passo 2: Ler 5 números inteiros do usuário
print("Digite 5 números:")
for i in range(5):
    numero = int(input(f"Digite o {i+1}º número: "))
    vetor.append(numero)

# Passo 3: Mostrar os números na ordem em que foram digitados
print("\nNúmeros na ordem digitada:")
print(vetor)

# Passo 4: Mostrar os números na ordem inversa
print("\nNúmeros na ordem inversa:")
# O fatiamento [::-1] ou reversed() criam uma cópia da lista invertida
print(vetor[::-1])