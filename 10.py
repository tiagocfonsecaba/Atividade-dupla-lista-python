import os
os.system ("cls")



idades = []


while len(idades) < 5:
    idade = int(input(f"Digite a idade da pessoa {len(idades) + 1} (0 a 120): "))
    
    
    if 0 <= idade <= 120:
        idades.append(idade)
    else:
        print("Idade inválida! Por favor, digite um valor entre 0 e 120.")


maior_idade = max(idades)
menor_idade = min(idades)


maiores_de_18 = len([id for id in idades if id >= 18])


print("\n--- Resultados ---")
print(f"Idades digitadas: {idades}")
print(f"Maior idade: {maior_idade} anos")
print(f"Menor idade: {menor_idade} anos")
print(f"Quantidade de maiores de idade: {maiores_de_18}")
