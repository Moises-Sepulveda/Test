#!/usr/bin/env python3
#_*_ coding: utf8 _*_

#SUMADORA EN PYTHON3 - Cybersecurity Expert

#Declaración de función para sumar dos valores, tiene como argumentos 
#dos valores de entrada, a y b, y devuelve la suma de estos dos valores.
def sumadora(a,b):
    return a+b

#ENTRADA DE DATOS DE VALORES COMO FLOTANTES
num1 = int(input("Introduce el primer valor: "))
num2 = int(input("Introduce el segundo valor: "))

#Llamamos la función sumadora e imprimimos el resultado de su operación por pantalla,
#como se puede ver le pasamos dos parámetros, el num1 y num2.
print("\nEl resultado de la suma es:",sumadora(num1,num2))


