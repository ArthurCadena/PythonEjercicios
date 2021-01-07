#Pide dos números. Si el primero es mayor que el segundo, muestre primero el 
#segundo número y luego el primer número; de lo contrario, muestre primero 
#el primer número y luego el segundo.

num1  = int(input("Inserta un numero:"))
num2 = int(input("Inserta otro numero:"))

if num1 > num2:
    print(num2, num1)
else:
    print(num1, num2)

