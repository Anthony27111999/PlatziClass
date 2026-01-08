texto = "Hola mundo"

# saber el largo
print(len(texto))

texto = "clase de python"
#Busqueda en el texto
Inclusion = "python" in texto
print(Inclusion)

noInclusion = "javascript" not in texto
print(noInclusion)

# mayusculas
texto = texto.upper()
print(texto)

#Minusculas
texto = texto.lower()
print(texto)

# borrar espacios
sinEspacios = "     ejempo    ".strip()
print(sinEspacios)

texto = "Este es un texto"

#Cortar texto
print(texto[0:5])

# Remplazar
curso = 'Este curso es de C#'
print(curso.replace('C#', 'Python'))

#Dividir texto
txto_dividido = curso.split(' ')
print(txto_dividido)

# Normalizacion -> Si quiero buscar palabras y no se si tiene mayuscula o minuscula
print("c#".lower() in txto_dividido.lower())