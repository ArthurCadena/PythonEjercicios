#Pídale al usuario que ingrese su color favorito. Si ingresan "rojo", "ROJO" o "Rojo", muestra el mensaje
#"A mí también me gusta el rojo", de lo contrario, muestra el mensaje "No me gusta [color], prefiero el rojo".

color = input("Ingresa tu color favorito:")
color = str.lower(color)
if color == "rojo" :
    print("A mi tambien me gusta el rojo :) !!")
else:
    print("No me gusta el " + color + " prefiero el rojo")

