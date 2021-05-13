#!/usr/bin/env python3
#_*_ coding: utf8 _*_

#CALCULO DE SUPERFICIE DE UN CUADRADO

#La formula para calcular la superficie de un cuadrado es la base multiplicada por sí misma.

print("CALCULO DE SUPERFICIE DE UN CUADRADO\n")


#Función para calcular la superficie, recibe como argumento la base del cuadrado.i

def SuperficieCuadrado(base):
    return base**2

#ENTRADA DE DATOS POR TECLADO
int_base = int(input("INTRODUCE LA BASE DEL CUADRADO: "))

print("\nLa superficie del cuadrado es:",SuperficieCuadrado(int_base))
