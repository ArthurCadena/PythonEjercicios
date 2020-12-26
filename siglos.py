#programa que calcula el siglo en el que nos encontramos segun el año

import math
def siglo():
    año = int(input("Introduce un año:"))
    total = math.floor(año)/100
    total = math.floor(total)
    sigloT = total + 1
    print("Nosotros estamos en el siglo " + str(sigloT))

siglo()

