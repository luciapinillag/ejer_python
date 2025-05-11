estudiantes = int(input("Ingrese cantidad de estudiantes: "))
notas = []

# Pedir las notas de cada estudiante
for i in range(estudiantes):
    nota = float(input(f"Ingrese la nota del estudiante {i+1}: "))
    notas.append(nota)

# Calcular promedio
promedio = sum(notas) / len(notas)

# Calcular cuántas notas están bajo el promedio
bajo_promedio = 0
for nota in notas:
    if nota < promedio:
        bajo_promedio += 1

# Mostrar resultados
print("===")
print("Notas ingresadas:", notas)
print("Promedio general:", promedio)
print("Cantidad de notas bajo el promedio:", bajo_promedio)
print("Nota más alta:", max(notas))
print("Nota más baja:", min(notas))
print("¿Está la nota 7.0 en la lista?", 7.0 in notas)
print("Notas ordenadas:", sorted(notas))
