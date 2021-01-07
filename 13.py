#Pídale al usuario que ingrese un número menor de 20. Si ingresa un número que 
#es 20 o más, muestre el mensaje "Demasiado alto"; de lo contrario, muestre "Gracias".

men20  = int(input("Ingresa un numero menor a 20:"))

if men20 >= 20:
    print("Demasiado alto:")
else:
    print("Gracias!!")