#Pídale al usuario que ingrese 1, 2 o 3. Si ingresa un 1, muestre el mensaje "Gracias", si ingresa un 2, 
#muestre "Bien hecho", si ingresa un 3, muestre "Correcto". Si ingresan algo más, muestra "Mensaje de error".

num = int(input("Ingresa el numero 1, 2 ó 3:"))

if num == 1:
    print("Gracias")
elif num == 2:
    print("Bien hecho")
elif num == 3:
    print("Correcto")
else:
    print("Error error error autodestruccion programada en 10 segundos X_X !!")