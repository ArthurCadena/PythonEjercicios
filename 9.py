#Escriba un programa que solicite una cantidad de días y luego muestre cuántas horas, 
# minutos y segundos hay en esa cantidad de días.
print("CALCULA LAS HORAS,MINUTOS Y SEGUNDOS DE LOS DIAS \n************************************************")
dias = int(input("Ingresa el numero de dias:"))
horas = dias * 24
minutos = horas * 60
segundos = minutos * 60

print("En " + str(dias) + " dia(s) hay " + str(horas) + " horas, " + str(minutos) + " minutos y " + str(segundos) + " segundos")
