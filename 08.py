import os
os.system ('cls')


nomes = []
salarios = []

for i in range(5):
    nome = input(f"Digite o nome do {i+1}º funcionário: ")
    salario = float(input(f"Digite o salário de {nome}: R$ "))
    
    nomes.append(nome)
    salarios.append(salario)


maior_salario = max(salarios)
posicao_maior = salarios.index(maior_salario)
nome_maior_salario = nomes[posicao_maior]


acima_dois_mil = 0
for salario in salarios:
    if salario > 2000:
        acima_dois_mil += 1


print("\n--- RESULTADOS ---")
print(f"Funcionário com o maior salário: {nome_maior_salario} (R$ {maior_salario:.2f})")
print(f"Quantidade de funcionários que ganham acima de R$ 2.000,00: {acima_dois_mil}")
