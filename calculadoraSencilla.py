print("CALCULADORA SENCILLA \n******************************************************")
print("Menú:")
print("1.-sumar 2 numeros \n2.-restar 2 numeros \n3.-multiplicar 2 numeros \n4.-dividir 2 numeros")
menu = int(input("Ingresa una opcion del menu:"))
a = float(input("Ingresa el primer numero:"))
b = float(input("Ingresa el segundo numero:"))

def suma(a, b):
    total = a + b
    return print("La suma de a + b es:" + str(total))
def resta(a, b):
    total = a - b
    return print("La resta de a - b es:" + str(total))
def multiplicacion(a, b):
    total = a * b
    return print("La multiplicacion de a * b es:" + str(total))
def division(a, b):
    total = a / b
    return print("La division de a / b es:" + str(total))

if menu == 1:
    suma(a, b)
elif menu == 2:
    resta(a, b)
elif menu == 3:
    multiplicacion(a, b)
elif menu == 4:
    division(a, b)
