N = int(input("Ingrese la cantidad de numeros a promediar "))

sumaAcumulada = 0

for i in range (0, N):
    numero = float(input("ingrese numeros a promediar "))

    sumaAcumulada = sumaAcumulada + numero

promedio = sumaAcumulada / N
print("el promedio de los numeros ingresados es ", promedio)