auto ={
    "marca": "Toyota",
    "color": "Rojo",
    "Anio": 1999
}

# ver el valor de una clave 
print(auto["marca"])
print(auto.get("marca"))

# Saber las claves
print(auto.keys())
# Saber los valores
print(auto.values())

if "Toyota" in auto:
    print(f"La marca es: {auto.get('marca')}")

## Agregar propiedades
auto["Dueño"] = 'Marcos'
print(auto["Dueño"])

#Para modificar o agregar
auto.update({"Dueño":"Anthony", "Puertas": 4})
print(auto)

# Bucles
# Ver keys
for k in auto:
    print(k)

# Ver valores
for v in auto.values():
    print(v)

# Recorrer ambos a la vez
for k,v in auto.items():
    print(k, " : ", v)

# Leer objetos dentro de objetos
automotora = {
    "Auto1" : {
        "Marca": "Renault",
        "año": 2000
    },
    "Auto2" : {
        "Marca": "Renault",
        "año": 1967
    }
}

print(automotora["Auto2"]["año"])
# Elimina el item seleccionado
auto.pop("Dueño")
print(auto)

# Elimina la ultima propiedad del diccionario
auto.popitem()
print(auto)

# Vacias diccionario
auto.clear()
print(auto)