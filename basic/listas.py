frutas = ["Manzana", "Naranja", "Mandarina", "Kiwi"]

#Buscar elementos
print(frutas[0])

#Cambiar elemento
frutas[1] = "Banana"

#Saber el largo
print(len(frutas))

#get range of list
print(frutas[0:2])

# Verificar existencia de elementos en una lista
if "Kiwi" in frutas:
    print("esta copada esta propiedad")

# Metodos de listas

frutas.append("Uva")
print(frutas)

# Agregr en un indice
frutas.insert(2, "Sandia")
print(frutas)

# Eliminar elementos
frutas.remove('Uva')
print(frutas)

# Eliminar elementos por indice
frutas.pop(1)
print(frutas)

# ordenar alfabetico
numeros = [1,2,3,4]
frutas.sort()
numeros.sort()

# ordenar inverso a alfabetico
frutas.reverse()
print(frutas)

# Union de listas
verduras = ["Cebolla", "Morron"]

comidas = verduras + frutas

print(f"Comidas: {comidas}")

# Extend modifica la lista que este instanciada
verduras.extend(frutas)
print(verduras)