#generar un programa que pida al usuario ingresar un numero e imprima, "es uno" si ingresa uno, es dos si ingresa un dos, es tres si ingresa un tres o cuatro, o no es 1,2,3,4 si se ingresa otro numero.

num = int(input("Ingresa un numero "))
if(num == 1):
    print("ES UNO")
elif(num == 2):
    print("ES DOS")
elif(num == 3):
    print("ES TRES")
elif(num == 4):
    print("ES CUATRO")
else:
    print("NO ES 1, 2, 3 NI 4")