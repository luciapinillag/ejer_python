#ejecutar un programa que permite ingresar una cantidad  N de notas donde n fue definido por el usuario e imprime el promedio de dichas notas, ademas l programa valida cada nota ingresada de manera que siempre sean notas validas entre 1.0 y 7.0

N = int(input("Ingrese la cantidad de notas "))

sumaAcumulada = 0

for i in range (0,N):
    var = True
    while(var):
        nota = float(input("Ingrese notas a promediar"))
        if(nota < 1 or nota > 7):
            print("Nota no valida...reintente")
        else:
            sumaAcumulada = sumaAcumulada + nota
            var = False

promedio = sumaAcumulada / N
print("El pomedio de las notas ingresadas es: ", promedio)