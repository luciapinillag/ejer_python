from operator import truediv

import sumar as S
import restar as R
import multiplicar as M
import dividir as D
import factorial as F

continuar = True

while(continuar):
    opcion = input(" Ingrese 0 para salir, 1 para sumar, 2 para restar, 3 para multiplicar o 4 para dividir: ")
    if(opcion == "0"):
        print("gracias por usar la calculadora")
        continuar = False
    else:
        num1 = int(input("ingrese un numero: "))
        num2 = int(input("ingrese otro numero: "))
        if(opcion == "1"):
            resultado = S.sumar(num1, num2)
            print(" la suma de ambos numeros es: ", resultado)
        elif(opcion == "2"):
            resultado = R.restar(num1, num2)
            print(" la resta de ambos numeros es: ", resultado)
        elif(opcion == "3"):
            resultado = M.multiplicar(num1, num2)
            print("la multiplicacion de ambos numeros es: ", resultado)
        elif(opcion == "4"):
            resultado = D.dividir(num1, num2)
            print("la division de ambos numeros es: ", resultado)

num = int(input("ingrese un numero: "))
respuesta = F.factorial(num)
print(" la factorial del: ", num, "es", respuesta)