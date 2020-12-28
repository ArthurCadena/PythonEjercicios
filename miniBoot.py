import pyautogui, time #librerias y modulos necesarios documentacion en la descripcion del canal
pyautogui.sleep(5) #ponganle mas de 5 segundos para que les de tiempo XD 
f = open("terminator", "r") #

for palabra in f:
    pyautogui.typewrite(palabra)
    pyautogui.press("enter")
