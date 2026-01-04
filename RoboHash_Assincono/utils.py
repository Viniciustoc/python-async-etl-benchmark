import aiohttp
import asyncio
import aiofiles

async def get_url_async(session, base_url, id_foto):
    """
    Objetivo: Gerar url, efetuar o request na api utilizando funções assincronas, e retornar a url de download
    """
    url = f'{base_url}/{id_foto}' # Gera a url completa concatenando com id_foto
    try: # try para maior resiliencia do code
        async with session.get(url) as response: # efetua a request na url
            response.raise_for_status() # Utilizado para erro imedito e pausa do sistema
            data = await response.json() # Retorna os dados com await, para que aguarde o download dos dados
            return data['url'] # Retorna a url
    except Exception as e:
        print(f'Erro na API: {e}')
        return None

async def download_image_async(session, url, filename):
    """
    Objetivo: Efetuar o download do arquivo na pasta do arquivo main
    """
    async with session.get(url) as response_img:
        try:
            response_img.raise_for_status()
            content = await response_img.read()
            async with aiofiles.open(filename, 'wb') as f: await f.write(content)
            return True

        except Exception as e:
            print(f'Erro ao efetuar o download: {e}')
            return None
