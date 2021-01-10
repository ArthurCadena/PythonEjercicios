#Pregúntele al usuario si está lloviendo y convierta su respuesta a minúsculas para que no importa en 
#qué caso lo escriba. Si responde "sí", pregunte si hace viento. Si responden "sí" a esta segunda pregunta, 
#muestre la respuesta "Hace demasiado viento para un paraguas"; de lo contrario, muestre el mensaje "Tome un paraguas". 
# Si no respondió afirmativamente a la primera pregunta, muestre la respuesta "Disfrute su día".
lluvia = input("Esta lloviendo?:")
lluvia = str.lower(lluvia) #cambiamos el valor de la variable pregunta a un string en minusculas

if lluvia == "si":
    viento = input("Hace viento?:")
    viento = str.lower(viento)
    if viento == "si":
        print("Hace demasiado viento para un paraguas X_X !!")
    else:
        print("Toma un paraguas :D !!")
else:
    print("Disfrute su dia :P !!")