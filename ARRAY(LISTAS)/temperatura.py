n = int(input(" ingrese la cantidad de temperatura a registar "))
temperaturas = []
print("===")
for i in range (0, n):
    tem = float(input(" ingrese la temperatura"))
    temperaturas.append(tem)
    print("===")
    suma = sum(temperaturas)
    promedio = suma/n
    print("el promedio de las temperaturas es ", promedio)
    print("===")
    cantidad = 0

    for i in range (0, n):
        if(temperaturas[i] <promedio):
            cantidad = cantidad + 1
    print("hay", cantidad, "temperaturas bajo el promedio")
    print("===")