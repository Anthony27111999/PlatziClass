# Conjunto: Coleccion de elementos no ordenado y unicos (Set)

saludos = {'Hola', 'Como estas?', 'Buen dia'}

# Recorrer
for saludo in saludos:
    print(saludo)

# Agregar

saludos.add("Buenas tardes")
print(saludos)
saludos.update(['buenas'],{'Good morning', 'Good afternoon',('Buenas tardes2')})
print(saludos)

# Borrar 
# Remove puede dar error si no esta el elemento
saludos.remove('Buenas tardes2')
print(saludos)
saludos.discard('buenas')
print(saludos)
# pop elimina un elemento al azqar
saludos.pop()
print(saludos)

# Limpiar el conjunto
saludos.clear()
print(saludos)


print("------------------------- Operaciones entre conjuntos ---------------------------")

a = {"a", "b", "c"}
b = {"c", "d", "e"}

# el conjunto a y b (Union)
c = a.union(b)
print(c)

# Interseccion
c = a.intersection(b)
print(f"interseccion {c}")

#Diferencia
d = a.difference(b)
print(d)
a = 7
print(a.__str__())