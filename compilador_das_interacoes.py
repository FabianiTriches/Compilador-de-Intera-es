import json
import os

# caminho da pasta que sera executado o script
pasta = 'D:/Users/fabia/Documents'
# lista que guardara todos os resultados
valores_propriedade = []
# lista que guardara o nome de todos os arquivos com resultados
nomes_arquivos = []

# percorre todos os arquivos da pasta um a um
for arquivo in os.listdir(pasta):
    # verifico se o arquivo termina em .json e se sim, continua
    if arquivo.endswith('.json'):
        # adiciono o nome do arquivo na lista nomes_arquivos 
        # print(arquivo)
        nomes_arquivos.append(arquivo)
        # monto o caminho do arquivo para ser lido e extraida as infos
        caminho_arquivo = os.path.join(pasta, arquivo)
        # abro cada arquivo
        with open(caminho_arquivo) as file:
            # faco o load dos dados
            data = json.load(file)
            # acesse a propriedade desejada do arquivo JSON
            propriedade = data['texts3d']['texts']
            # concatenar os elementos da lista em uma única string separados por vírgula
            string_linha = ', '.join(propriedade)
            # adiciono os valores na lista valores_propriedade 
            valores_propriedade.append(string_linha)

# nome arquivos gerados, um contendo o conteudo e o outro os nomes dos arquivos
conteudo_arquivos = 'D:/Users/fabia/Documents/conteudo_arquivos.txt'
nome_arquivos = 'D:/Users/fabia/Documents/nome_arquivos.txt'

# adiciono no arquivo conteudo_arquivos.txt os resultados
with open(conteudo_arquivos, 'w') as file:
    for valor in valores_propriedade:
        file.write(str(valor) + '\n')

# adiciono no arquivo nome_arquivos.txt os nomes dos arquivos
with open(nome_arquivos, 'w') as file:
    for nome in nomes_arquivos:
        file.write(str(valor) + '\n')