import requests
import os
import datetime

def newsapi_client(api_key, query, timeout=30, retries=3) -> dict:
    """
        Extraemos la informacion de las noticias de <strong>https://newsapi.org/</strong>
    """
    try:
        today = datetime.datetime.today()
        url =f'https://newsapi.org/v2/everything?q=Apple&from={today.year}-{11}-{today.day}&\sortBy=popularity&apiKey={api_key}'
        response = requests.get(url).json()
        return response
    except apiKeyInvalid as a:
        return [f"{e}"]
    except Exception as e:
        return [f"Error al querer carga la informacion. Error: {e}"]

def guardian_client(api_key, query, timeout=30, retries=3):
    print(f"api_key{api_key}\nquery{query}\ntimeout{timeout}\nretries{retries}")
    pass

def fetch_news(api_name, *args, **kwards):
    """
    Funcion base para todas las API's
    """

    config_base = {
        "timeout": 0,
        "retries": 3,
    }

    #Cuanod llamamos a las variables con ** nos hace como un mapeo por cada variable dentro de los dic
    config = {
        **config_base,
        **kwards
    }

    api_clientes = {
        "newsapi": newsapi_client,
        "guardian": guardian_client,
    }

    client = api_clientes[api_name]
    return client(*args, **config)
