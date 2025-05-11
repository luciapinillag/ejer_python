#generar un programa que pida la usuario ingresar dos numeros e imprima el mensaje, el numero mayor es < numero mayor de los ingresados >, si son iguales, lo debera indicar

num1 = int(input("Ingresar el primer numero "))
num2 = int(input("Ingresar el segundo numero "))
if(num1 > num2):
    print(f"el numero mayor es:{num1} ")
elif(num2 > num1):
    print(f"el numero mayor es:{num2} ")
else:
    print("los numeros ingresados son iguales")

 
