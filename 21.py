#Pídale al usuario que ingrese su nombre y luego pídale que ingrese su apellido. 
#Únelos con un espacio entre ellos y muestre el nombre y la longitud del nombre completo.
nombre = input("Introduce tu primer nombre:")
apellido = input("Introduce tu apellido:")
resultado = len(nombre) + len(apellido)
print("Hola " + nombre + " " + apellido + " la longitud de tu nombre es:" + str(resultado))