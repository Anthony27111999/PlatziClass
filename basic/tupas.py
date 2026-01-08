# metodos de las tuplas

tecnologias = ("Python", "Javascript", "C#", "Python")
print(tecnologias)

print(len(tecnologias))

# puedo separar cada elemento, pero tiene que ser la misma cantidad de elementos
x,y,z,m = tecnologias
print(f"{x} => {y} => {z}")

# Unir tuplas
tuppla = (0,1,2)
tupla_final = tuppla + tecnologias
print(tupla_final)

# podemos hacer que aparezcan  veces los elementos en la tupla
tuppla = tuppla *2
print(tuppla)