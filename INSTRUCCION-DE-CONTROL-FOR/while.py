#este programa enviara un mensaje no es un 1 mientras que el usuario no ingrese el valor 1
num = 0
while (num != 1):
    num = int(input("ingres un 1 para salir "))
    if (num != 1):
        print("no es un 1... reintente")

print("Muy bien!!! Logramos salir del ciclo while")