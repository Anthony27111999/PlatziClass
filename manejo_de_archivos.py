#Funcion basica de python para manejar archivos
#open(name, mode)
print(20 - 10/5 *2**2)
"""
    Los modos que tenemos son: 
        R (Read)
        W (Write)
        X (Crear archivos nuevos)
        a agrega
 """

# f = open("diccionario.py", "r")
# print(f.readline())
# f.close()

# #Crear archivos
# open("ejemplo2.txt", "x")


# # Para no tener que abrir y cerrar nosotros tenemos with
# with open("ejemplo.txt", "r", encoding="utf-8") as f:
#     print(f.readline())

# with open("ejemplo.txt", "w", encoding="utf-8") as f:
#     f.write("Texto nuevo x2 ")

# with open("ejemplo.txt", "a", encoding="utf-8") as f:
#     f.write("\nHola mundo ")


def write_news(news: dict, extension = 'txt'):
    """
    Escribimos las noticias en un archivo
    """
    with open(f"news.{extension}", "w", encoding='UTF-8') as f:
        f.write(str(news))