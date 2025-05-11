#el siguiente programa permite ingresar una cantidad "n" de notas donde n es definida por el usuario imprime el promedio de dichas notas, ademas el programa valida cada nota ingresada  de manera que siempre sean notas validas

N = int(input("ingresar la cantidad de notas a promediar"))

sumaAcumulada = 0
for i in range (0, N):
    var = True
    while(var):
        nota = float(input("ingrese notas a promediar"))
        if (nota <1 or nota >7):
            print("nota no valida.....Reintente")
        else:
            sumaAcumulada = sumaAcumulada + nota
            var = False

promedio = sumaAcumulada / N
print("el promedio de los numeros ingresados es ", promedio)
