#Pídale al usuario que ingrese tres números. Sume los dos primeros números y luego multiplique este 
# total por el tercero. Muestre la respuesta como La respuesta es [respuesta].
print("Programa que suma los 2 primeros numeros y multiplica el resultado \n *****************************")
num1 = float(input("Ingresa el primer numero:"))
num2 = float(input("Ingresa otro numero:"))
num3 = float(input("Ingresa el ultimo numero:"))
total = (num1 + num2)*(num3)
print("La respuesta es:" + str(total))
