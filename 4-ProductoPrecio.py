#!/usr/bin/env python3
#_*_ coding: utf8 _*_

#Declaración de función que sirve para calcular el precio
#por la cantidad. Recibe como argumentos el precio y la 
#cantidad, y retorna la multiplicación de estos.

def ProductCalc (prices,amount):
    return prices*amount

#Entrada de datos por teclado.
str_product_name = input("Introduce the name of the product: ")
int_product_prices = int(input("Introduce the prices of the product: "))
int_amount = int(input("Introduce the amount of product: "))

#Invocación de la función e impresión de datos por pantalla.
print("\nThe invoces make in total: ",ProductCalc(int_product_prices,int_amount))        
