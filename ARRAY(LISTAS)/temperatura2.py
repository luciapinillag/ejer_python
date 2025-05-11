n = int(input("Ingrese la cantidad de temperaturas a registrar: "))
temperaturas = []

print("===")

# Entrada de temperaturas
for i in range(n):
    tem = float(input("Ingrese la temperatura: "))
    temperaturas.append(tem)

print("===")

# Cálculo del promedio
suma = sum(temperaturas)
promedio = suma / n
print("El promedio de las temperaturas es:", promedio)
print("===")

# Conteo de temperaturas bajo el promedio
cantidad = 0
for i in range(n):
    if temperaturas[i] < promedio:
        cantidad += 1

print("Hay", cantidad, "temperaturas bajo el promedio")
print("===")
