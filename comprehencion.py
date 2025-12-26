import requests
import json
import time

users_list =[]

def Check_users() -> list:
    global users_list 
    if not users_list:
        users_list = GetUsers()
    return users_list

def GetUsers() -> list:
    """
    Extrae usuarios de endpoint
    
    :return: Descripción
    :rtype: list
    """
    try:
        url = 'https://jsonplaceholder.typicode.com/users'
        users = requests.get(url=url)
        return users.json()
    except requests.RequestException as e:
        print(f"Error en la llamada:{e}")
        return []
    
def get_names(x, list_element: list):
    """
    Extrae los nombres cuando sean mas chicos que x caracteres
    
    :param list_element: Descripción
    :type list_element: list
    """
    # Podemos agregar condiciones al final
    return [t["name"] for t in list_element if len(t["name"]) < x]

def print_keys(consult):
    if consult:
        print(consult[0].keys())

def get_properties(users: list) -> dict[int, str]:
    if users: 
        return {user['id']: user['name'] for user in users}


inicio = time.perf_counter()
retorno = Check_users()
print(get_names(20, retorno))
print_keys(Check_users())
users = get_properties(retorno)
for user in users:
    print(f"-- \nNumero de usuario: {user} \nNombre {users[user]} \n--")
final = time.perf_counter()
print(f"Tiempo = {final - inicio}")
