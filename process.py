import os
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()
    pass

def stoping_process():
    print("Que proceso de los siguientes desea detener: \n 1. Explorador de archivos\n 2. Telegram\n 3. Chrome")
    opcion = int(input("Que opcion desea: "))
    if opcion == 1:
        try:
            talk("Deteniendo proceso...")
            os.system("taskkill /IM explorer.exe")
            talk("Proceso detenido")
        except:
            talk("Ocurrio un error mientras se intentaba detener el proceso")
            pass
    if opcion ==2:
        try:
            talk("Deteniendo proceso...")
            os.system("taskkill /IM Telegram.exe")
            talk("Proceso detenido")
        except:
            talk("Ocurrio un error mientras se intentaba detener el proceso")
            pass
    if opcion ==3:
        try:
            talk("Deteniendo proceso...")
            os.system("taskkill /IM chrome.exe")
            talk("Proceso detenido")
        except:
            talk("Ocurrio un error mientras se intentaba detener el proceso")
            pass
        
def init_process():
   talk("Seleccione el proceso que desea iniciar")
   print("Procesos:\n 1. Telegram \n 2. Chrome\n")
   opcion = int(input("Opcion: "))
    
   if opcion ==1:
       try:
           talk("Iniciando el programa")
           os.startfile(r"C:\\Users\CUBA\Downloads\Compressed\Telegram\Telegram.exe")
           talk("Programa inciado")
       except:
           talk("Ha ocurrido un error en la inicializacion del programa Telegram")
           pass
   elif opcion==2:
       try:
           talk("Iniciando programa")
           os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
           talk("Programa inciado")
       except:
           talk("Ha ocurrido un error en la incializacion del programa Chrome")

    