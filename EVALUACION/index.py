import ejercicio1 as n
from EVALUACION.bajo_promedio import bajoPromedio
from EVALUACION.promedio import calcular_promedio

lista = [8, 16, 14, 24, 32]
print(n(lista))

n =int(input("ingrese las notas"))
notas = ingresar_notas(N)

promedio = calcular_promedio(notas)

print("notas ingresadas: ", notas)

print("promedio notas: ", promedio)

print("notas bajo el promedio: ", bajoPromedio)