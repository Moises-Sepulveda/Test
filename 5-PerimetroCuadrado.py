#!/usr/bin/env python3
#_*_ coding: utf8 _*_

#Declaración de función que acepta un lado del cuatrado como argumento y devuelve su perimetro
def PerimeterCalc(side):
    return side*4

#Entrada de datos por teclado
int_squareSide=int(input("Hello! Introduce a side square value: "))

#Impresión del resultado por pantalla
print("\nThe Perimeter is: ",PerimeterCalc(int_squareSide))
