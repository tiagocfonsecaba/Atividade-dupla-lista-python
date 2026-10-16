import os 
os.system('cls')

vetor = []
dias_da_semana = 7



for i in range (dias_da_semana):
    temperatura = float(input(f'digite a temperatura de hoje: {dias_da_semana}'))
    temperatura.append()
    
    media = sum(temperatura) / len(temperatura)
    maior = max(temperatura)
    menor = min(temperatura) 
    
    print('\n = Exibindo Temperatura da semana') 
    print(f'Maior temperatura: {temperatura}')
        
                    