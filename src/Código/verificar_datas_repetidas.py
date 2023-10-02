from collections import Counter
import re

def encontrar_datas_repetidas(caminho_arquivo):
    # Abre o arquivo
    with open(caminho_arquivo, 'r') as arquivo:
        # Lê todas as linhas do arquivo
        linhas = arquivo.readlines()

        # Encontra todas as datas nas linhas
        datas = re.findall(r'\d{4}-\d{2}-\d{2}', ' '.join(linhas))

        # Conta quantas vezes cada data aparece
        contagem_datas = Counter(datas)

        # Retorna as datas repetidas
        datas_repetidas = [data for data, contagem in contagem_datas.items() if contagem > 1]

    return datas_repetidas

# Exemplo de uso
caminho_arquivo = 'src/Dados/Arquivos_Aleatórios/Arquivo_Aleatório_10000.txt'
datas_repetidas = encontrar_datas_repetidas(caminho_arquivo)

if datas_repetidas:
    print(f"As datas repetidas são: {', '.join(datas_repetidas)}")
else:
    print("Não foram encontradas datas repetidas.")