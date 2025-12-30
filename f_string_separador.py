def separador():
    sueldo=100000
    text = f"Saldo = {sueldo:,}"

    print(text)

def toma_de_decimales():
    cantidad = 1.098

    print(f"cantidad en 1 fraccion = {cantidad:.1f}")
    print(f"cantidad en 2 fracciones = {cantidad:.2f}")

    #Tiene que ser int
    cantidad = 19
    print(f"Agregamos 0 a la izquierda: {cantidad:08d}")

#Como no conocia esto??!!! (carita de asombro)
def alinear_texto():
    nombre = 'Anthony'
    apellido = 'Sosa'

    texto = f"Nombre: {nombre:>10} || Apellido: {apellido:>10}"
    print(texto)

def fechas():
    from datetime import datetime
    date = datetime(2025, 12, 29, 7, 11)
    print(f"Fecha del dia:\nDia:{date:%A}-{date:%d}\nAño:{date:%Y}\nMes:{date:%B}\nHora:{date:%I:%M %p}")