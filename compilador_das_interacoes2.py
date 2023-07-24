import pandas as pd
import json
import os

pasta = 'D:/Users/fabia/Documents'

valores_propriedade = pd.DataFrame()

for arquivo in os.listdir(pasta):
    if arquivo.endswith('.json'):
        caminho_arquivo = os.path.join(pasta, arquivo)
        with open(caminho_arquivo) as file:
            data = json.load(file)
            # Acesse a propriedade desejada do arquivo JSON
            propriedade = data['texts3d']['texts']
            
            valores_propriedade.append(propriedade)

arquivo_txt = 'D:/Users/fabia/Documents/saida.txt'
with open(arquivo_txt, 'w') as file:
    for valor in valores_propriedade:
        file.write(str(valor) + '\n')