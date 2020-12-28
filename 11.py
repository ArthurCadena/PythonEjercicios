#Solicite al usuario que ingrese un número superior a 100 y luego ingrese un número menor de 10 y 
#dígale cuántas veces el número menor entra en el número mayor en un formato fácil de usar.
nmayor = int(input("Ingresa un numero entero mayor a 100:"))
nmenor = int(input("Ingresa un numero entero menor a 10:"))

total = nmayor // nmenor

print("El numero "+ str(nmenor) +" cabe " + str(total) + " veces en el " + str(nmayor))

