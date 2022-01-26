from ast import Return
import math

#This program don't use API, so you need to refresh the prices

euro= 1
Pesos= 200
print ("::::::::::   THE PRICE OF THE CURRENCY FOR TODAY  ::::::::::\n")
print(f"Euro price: {euro}")
print(f"Peso Argentino price: {Pesos}")
print ("\nwhat change do you want to make??")
print("\t" "1.-Euro to Pesos Argentinos\n\t"  "2.-Pesos Argentinos to Euro \n")

Opc=int(input("Seleccion your option:\n"))
nom=input(str("Introduce your Name:\n  "))
quant_to_change=int(input("Now, add the amount you want to change:\n"))

def calculation (Opc):
    if  Opc == 1:
        print (quant_to_change * Pesos)
    elif Opc == 2:
        print (quant_to_change / Pesos)
    else:
        print ("Please select just 1 or 2")


print("Mr/Mrs ", nom ) 
print ("The ammount is: ")
print (calculation(Opc))
print ( ":::::: THANK YOU ::::::" ) 