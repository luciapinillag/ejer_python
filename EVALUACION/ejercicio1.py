# solicitar cantidad de numeros
numero = int(input("ingrese cantidad de numeros a registrar: "))

listaNumeros = []  # se guardan los numeros en la lista

# encuentra el tercer numero mayor
for i in range(numero):
    num = int(input("ingrese los numeros: "))
    listaNumeros.append(num)

# ordena la lista de los numeros
listaordenda = sorted(listaNumeros, reverse=True)

print("el tercer numero mayor es: ", listaordenda[2])

# cuenta los numeros impares
impares = 0
for numero in listaNumeros:
    if numero % 2 != 0:
        impares += 1

print("La cantidad de numeros impares es: ", impares)

#contar elementos mayores

mayores = 0

for i in range (1, len(listaNumeros)-1):
    actual = listaNumeros[i]
    izquierda = listaNumeros[:i]
    derecha = listaNumeros[i+1:]

    num_izq = any(x > actual for x in izquierda)
    num_dere =  any(x > actual for x in derecha)

    if num_izq and num_dere:
        mayores +=1
print("la cantidad de numeros entre dos mayores es: ", mayores)
