#Pídale al usuario que ingrese un número. Si es menor de 10, muestre el mensaje "Demasiado bajo", si su 
#número está entre 10 y 20, muestre "Correcto", de lo contrario muestre "Demasiado alto".

numero = int(input("Ingresa un numero:"))

if numero < 10 :
    print("Demasiado bajo!!")
elif numero >= 10 and numero<= 20:
    print("Correcto >:D !!")
else:
    print("Demasiado alto!!")