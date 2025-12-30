import time
import os

from dotenv import load_dotenv

from filtros import get_geo_classic, get_geo_pythonic
from matches import add_post_to_user_classic, user_to_post_compehencion
from f_string_separador import separador, toma_de_decimales, alinear_texto, fechas
from args_kwards import fetch_news
from manejo_de_archivos import write_news

load_dotenv()

input_option = int(input('Que ejecricio quieres?:'))
match input_option:
    case 1:
        inicio = time.perf_counter()
        geo = get_geo_classic()
        for g in geo:
            print(g)
        fin = time.perf_counter()
        print(f"Tiempo: {fin - inicio}")
    
    case 2:
        inicio = time.perf_counter()
        geo = get_geo_pythonic()
        for g in geo:
            print(g)
            print(type(g))
        print(type(geo))
        fin = time.perf_counter()
        print(f"Tiempo pythonic: {fin - inicio}")
    
    case 3:
        inicio = time.perf_counter()
        user_post = add_post_to_user_classic()
        print(user_post)
        fin = time.perf_counter()
        print(f"Tiempo pythonic: {fin - inicio}")
    
    case 4:
        inicio = time.perf_counter()
        user_post = user_to_post_compehencion()
        print(user_post)
        fin = time.perf_counter()
        print(f"Tiempo pythonic: {fin - inicio}")

    case 5:
        separador()

    case 6:
        toma_de_decimales()

    case 7:
        alinear_texto()

    case 8:
        fechas()

    case 9:
        API_KEY_NEWSAPI = os.getenv('api_news')
        news = fetch_news("newsapi", api_key= API_KEY_NEWSAPI, query='')
        write_news(news)
