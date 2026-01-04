import os
import time
import pandas as pd
from dotenv import load_dotenv
from utils import get_url, download_image

if __name__ == "__main__":
    start_time = time.time()
    load_dotenv() # carrega arquivos do dotenv, somente simulando o uso na api da nasa

    # URL para pegar os DADOS (Texto)
    base_url = "https://jsonplaceholder.typicode.com/photos" # Define a url base, que sera concatenada com o id_foto para gerar a url completa na função get_url

    dados_piloto = [] # Cria lista de dados vazia, para alocarmos os dados extraidos enquanto geramos o arquivo excel

    print("--- INICIANDO COLETA DE ROBÔS ---")

    for i in range(1, 51):
        print(f"Processando ID: {i}")

        url_original_quebrada = get_url(base_url, None, i) # Utilizamos essa url "quebrada" para simular o request na api da nasa, porem a mesma segue instavel, portanto, iremos utilizar a url_funcional

        status_download = 'N/A'
        nome_arquivo = 'N/A'

        url_funcional = f"https://robohash.org/{i}.png" # Essa é a url que de fato estamos usando, temporariamente ate que a url da nasa volte a funcionar

        if url_original_quebrada: # passamos a url quebrada para fins de estudo
            nome_arquivo = f'robo_{i}.png'
            if download_image(url_funcional, nome_arquivo): # realizamos o download na url funcional por enquanto
                status_download = 'Ok'
            else:
                status_download = 'Failed'
        else:
            status_download = 'Download Failed'

        # apendd dos dados extraidos na lista vazia criada no inicio do main
        dados_piloto.append({
            'ID': i,
            'Arquivo': nome_arquivo,
            'Status': status_download,
            'Fonte': 'RoboHash'
        })

        time.sleep(0.5)

    print('Gerando Excel...')
    df = pd.DataFrame(data=dados_piloto)
    df.to_excel('relatorio_robos.xlsx', index=False)

    end_time = time.time()
    print(f'Concluido! Tempo: {end_time - start_time:.2f} s')