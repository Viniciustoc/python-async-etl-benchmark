import requests


def get_url(base_url, api_key, id_foto):

    """
    Objetiv: Gerar a url completa concatenando o id_foto com a url base, essa api é uma api de teste, portanto nao exige parametros
    """
    url_completa = f"{base_url}/{id_foto}" # Criando a url completa para cada registro

    # Dando a request na api, utilizando try para maior resiliencia do codigo e raise_for_status para retorno do erro imediato
    try:
        response = requests.get(url=url_completa)
        response.raise_for_status()
        data = response.json()
        return data['url']  # Retorna a URL original (que vamos ignorar no main)

    except requests.exceptions.RequestException as errh:
        print(f'Erro na API: {errh}')
        return None


def download_image(url, filename):
    """
    Objetivo: Função de download padrão, realiza uma request fake na url, simulando o fluxo da api da nasa, utiliza try e raise_for_status para maior robustes
    """
    try:
        response_img = requests.get(url=url)
        response_img.raise_for_status()

        with open(filename, "wb") as arquivo:
            arquivo.write(response_img.content)

        print(f'Arquivo {filename} baixado')
        return True

    except requests.exceptions.RequestException as errh:
        print(f'Erro ao baixar: {errh}')
        return False


