import os
os.system ("cls")



vetor = []


print("Digite 8 números: ")
for i in range(8):
    numero = int(input(f"Posição {i}: "))
    vetor.append(numero)


busca = int(input("\nDigite um número para pesquisar: "))


if busca in vetor:
    posicao = vetor.index(busca)
    print(f"O número {busca} está na posição {posicao}.")
else:
    print("Número não encontrado")
