import os
import time
import asyncio
import aiohttp
import pandas as pd
from dotenv import load_dotenv

from utils import get_url_async, download_image_async

# Criaremos uma função que sera responsavevl por executar um robo por completo (url+download), isso facilita a organização do codigo

async def processar_robo(session, base_url, id_robo):

    url_fake = await get_url_async(session, base_url, id_robo) # Simular pegar dados da api

    status_download = 'n/a'
    nome_arquivo = 'n/a'

    url_funcional = f"https://robohash.org/{id_robo}.png" # Url real robohash

    if url_fake:
        nome_arquivo = f'robo_async_{id_robo}.png'
        # Baixa a imagem
        if await download_image_async(session, url_funcional, nome_arquivo):
            status_download = 'Sucesso'
        else:
            status_download = 'Erro'
    else:
        status_download = 'Erro API'

    return {
        'ID': id_robo,
        'Arquivo': nome_arquivo,
        'Status': status_download,
        'Modo': 'Assincrono'
    }


async def main():
    start_time = time.time()
    load_dotenv()

    base_url = 'https://jsonplaceholder.typicode.com/photos'

    tarefas = []

    print('Iniciando Robo Assíncrono')

    async with aiohttp.ClientSession() as session:
        for i in range(1, 201):
            task = processar_robo(session, base_url, i)
            tarefas.append(task)

        print(f'Disparando {len(tarefas)} tarefas simultâneas')

        restultados = await asyncio.gather(*tarefas)

    print('Gerando Excel...')

    df = pd.DataFrame.from_records(restultados)
    df.to_excel('relatorio_robo_async.xlsx', index=False)

    end_time = time.time()
    tempo_total = end_time - start_time
    print(f'Tempo total: {tempo_total}')

if __name__ == '__main__':
    asyncio.run(main())
