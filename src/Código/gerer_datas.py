from datetime import datetime, timedelta
import random

# Definindo a data inicial e final
start_date = datetime(1970, 1, 1)
end_date = datetime(2023, 10, 2)

# Lista para armazenar as datas
dates_list = []

# Gerando as datas
current_date = start_date
while current_date <= end_date:
    dates_list.append(current_date.strftime('%Y-%m-%d'))
    current_date += timedelta(days=1)

# Selecionando 1000 datas aleatórias
random_dates = random.sample(dates_list, 10000)

# Gravando as datas em um arquivo .txt
with open('src/Dados/Arquivos_Aleatórios/Arquivo_Aleatório_10000.txt', 'w') as file:
    for date in random_dates:
        file.write(date + '\n')

print("As datas foram gravadas no arquivo .txt")