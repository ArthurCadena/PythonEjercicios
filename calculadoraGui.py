from tkinter import *

ventana = Tk()
ventana.title("Calculadora")

i = 0 #lo creamos para las posiciones 

#Entrada
e_texto = Entry(ventana, font = ("Calibri 20"))
e_texto.grid(row = 0, column = 0, columnspan = 4, padx = 5, pady = 5)

#Funciones
def clickBoton(valor):
    global i #la declaramos para que se pueda usar esta variable fuera de la funcion 
    e_texto.insert(i, valor)
    i += 1

def borrar():
    e_texto.delete(0, END)
    i = 0

def operaciones():
    ecuacion = e_texto.get()
    resultado = eval(ecuacion)#lo se tanto trabajo para esto xD !!
    e_texto.delete(0, END)
    e_texto.insert(0, resultado)
    i = 0

symbols = {
    'botonParentesis': '(',
    'botonParentesis2': ')',
    'botonPunto': '.',
    'botonDiv': '/',
    'botonMult': '*',
    'botonSum': '+',
    'botonRest': '-'
    }

# Botones
for number in range(1, 10):
    exec(f"boton{str(number)} = Button(ventana, text = str(number), width = 5, height = 2, command = lambda: clickBotton(number))")

for key, values in symbols.items():
    exec(f"{key} = Button(ventana, text = values, width = 5, height = 2, command = lambda: clickBotton(values))")

boton0 = Button(ventana, text = "0", width = 13, height = 2, command = lambda: clickBoton(0))
botonBorrar = Button(ventana, text = "AC", width = 5, height = 2, command = lambda: borrar())
botonIgual = Button(ventana, text = "=", width = 5, height = 2, command = lambda: operaciones())

#Agregar botones en pantalla.
# for number in range(3):
counter = 0
counting = 1
butons = [
    botonParentesis, 
    botonParentesis2, 
    botonDiv, 
    boton7, 
    boton8, 
    boton9, 
    botonMult, 
    boton4, 
    boton5, 
    boton6, 
    botonSum, 
    boton1, 
    boton2, 
    boton3, 
    botonRest,  
    # botonPunto,
    # botonBorrar, 
    # botonIgual
    ]

counter = 0
counting = 1
for buton in butons:
    if (counter < 3):
        counter += 1
    else:
        counting += 1
        counter = 0
    
    buton.grid(row = counting , column = counter, padx = 5, pady = 5)

ventana.mainloop()