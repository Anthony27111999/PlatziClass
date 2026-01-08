# La estructura es: lambda args:exprecion

x = lambda a, b : a ** b

print(x(2,4))

# Las lambdas normalmente se usan para crear funciones

def funciones(n):
    return lambda a : a * n

duplicador = funciones(2)
triplicador = funciones(3)

print(duplicador(2))
print(triplicador(2))