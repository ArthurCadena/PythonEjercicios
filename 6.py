#Pregunte con cuántas porciones de pizza comenzó el usuario y pregunte cuántas 
#porciones se ha comido. Calcule cuántos cortes les quedan y muestre la respuesta en un formato fácil de usar.
print("CALCULADORA DE PIZZA \n*******************************************")
pedazosPizza = int(input("¿Cuantos pedazos tiene la pizza?:"))
comio = int(input("¿Cuantos de pizza te comiste?:"))

total = pedazosPizza - comio

print("Te quedan " + str(total) + " rebanadas de pizza")