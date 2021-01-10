#Pregunte la edad del usuario. Si tienen 18 años o más, mostrar el mensaje "Puedes votar", si tienen 17 años, 
#mostrar el mensaje "Puedes aprender a conducir", si tienen 16 años, mostrar el mensaje "Puedes comprar un boleto 
#de lotería", si son menores de 16 años, muestre el mensaje "Puedes hacer truco o trato".

edad = int(input("Introduce tu edad:"))

if edad >= 18:
    print("Puedes votar :D !!")
elif edad == 17:
    print("Puedes aprender a conducir!!")
elif edad == 16:
    print("Puedes comprar un boleto de loteria!!")
else:
    print("Puedes pedir dulces de hallowen xD !!")


