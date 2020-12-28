#Pregunte por el precio total de la factura, luego pregunte cuántos comensales hay. 
#Divida la cuenta total por el número de comensales y muestre cuánto debe pagar cada persona.
print("REPARTIDOR DE CUENTA RESTAURANTE \n********************************")
factura = float(input("Introduce el precio a pagar por la cuenta:"))
comensales = int(input("¿Cuantos comensales hay?:"))
total = factura / comensales
print("Cada persona de la mesa debe pagar:" + str(total))
