import os
os.system ("cls")



temperaturas = []
dias_da_semana = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]


print("= Digite a temperatura para cada dia da semana: =")
for dia in dias_da_semana:
    temp = float(input(f"{dia}: "))
    temperaturas.append(temp)


media_semanal = sum(temperaturas) / len(temperaturas)
maior_temp = max(temperaturas)
menor_temp = min(temperaturas)


print("\n--- RESULTADOS DA SEMANA ---")
print("Temperaturas registradas:")
for i in range(7):
    print(f"- {dias_da_semana[i]}: {temperaturas[i]}g")

print(f"\nMédia semanal: {media_semanal:.2f}g")
print(f"Maior temperatura: {maior_temp}g")
print(f"Menor temperatura: {menor_temp}g")