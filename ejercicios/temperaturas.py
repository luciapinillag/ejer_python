cantidad = int(input("¿Cuántas temperaturas vas a ingresar?: "))
temperaturas = []

for i in range(cantidad):
    temp = float(input(f"Ingrese la temperatura #{i + 1}: "))
    temperaturas.append(temp)

promedio = sum(temperaturas) / len(temperaturas)

print("===")
print("Temperaturas registradas:", temperaturas)
print("Promedio:", promedio)
print("Temperatura más alta:", max(temperaturas))
print("Temperatura más baja:", min(temperaturas))
