# sintaxis
import sys
_name = 'nombre de variable para variables privadas'
MAYUSCULAS = 'Variables constantes'

#Asignar varios valores a distintas variables
x,y,z = "1","2","3"
#print(x,y,z)
#sys.stdout.write('hola')
a = b = c = 'Manzana'
#print(a,b,c)
c = 'tomate'
#print(a,b,c)

# tipos de datos
stringType = 'tipo texto'

#numeros
a = 1 # int
print(type(a))
b = 3.14 # float
print(type(b))
c = 2 + 3j # complex
print(type(c))
print(c + a)

# List -> Colecciones ordenadas y mutable de elementos 
lista = [0,1,2,3,4,5,6,7,8,9]

# Tuplas -> Colecciones ordenadas e inmutables
tupla = (1,2,3)

# Diccionario -> Coleccion ordenada de parez clave : valor
diccionario ={
    "clave":"valor"
}

# Conjuntos (sets) -> coleccion desordenada mutable pero de elementos unicos
conjunto = {1,1,2,2,3}
print(conjunto) # -> {1, 2, 3}

# boolean
booleano = True | False





#conditional
if 5 >3:
    print("5 es mayor a 3")
    
