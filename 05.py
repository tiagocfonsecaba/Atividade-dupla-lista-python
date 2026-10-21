import os 
os.system('cls')

notas = []
soma = 0

for i in range(5):
    nota = float(input(f'digite a nota {i+1}º:    '))
    notas.append(nota)
    
    media = soma / 5
    
    acima_da_media = 0
    
    for nota in  notas:
        if nota > media :
            acima_da_media += 1
            
    print(f'Notas digitads: {notas}')
    print(f'media da turma: {media:.2f} ')
    print(f'Quantidades de notas acima da media: {acima_da_media}')