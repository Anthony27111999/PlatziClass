import requests
import json
import time

users_list =[]
post_list = []

def Check_users() -> list:
    global users_list 
    if not users_list:
        users_list = GetUsers()
    return users_list

post_list =[]

def Check_post() -> list:
    global post_list 
    if not post_list:
        post_list = get_post()
    return post_list

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
    
def get_post() -> list:
    """
    Extrae post de endpoint
    
    :return: Descripción
    :rtype: list
    """
    try:
        url = 'https://jsonplaceholder.typicode.com/posts'
        post = requests.get(url=url)
        return post.json()
    except requests.RequestException as e:
        print(f"Error en la llamada:{e}")
        return []