# Importamos las librerias

import os #Libreria estandar de Python
import datetime 
#import speech_recognition as sr # Libreria con el reconocimiento de voz en Python
import pyttsx3 # Libreria necesaria para acompañar al reconocimiento de voz en Python, sirve para las voces
import webbrowser 
import wikipedia as wp


from repara_danos import reparar
#from process import stoping_process
from dw_youtube import download

# Presentation of Program
class Template:

    def show_template(self):
        
        self.title = "Útiles"
        self.version = "7.0"
        self.author = "Rey Michel"
        self.description = "Programa con funciones muy utiles para el usuario. Esperemos que las disfrutes"
        
        print("--------------------------------")
        print(self.title)
        print(self.author)
        print(self.version)
        print(self.description)
        print("--------------------------------")
        
# Create a class called Programa
class Programa:
    def __init__(self):
        self.encendido = False
        self.encender = ""
        self.apagar = ""
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[2].id)
        pass
    
    def talk(self, text):
        self.engine.say(text)
        self.engine.runAndWait()
        pass
        

    def encender_wifi(self):
        if self.encendido == False:
            try:
                programa.talk("Especifique las credenciales de su zona wifi:")
                self.nombre_wifi = input("Nombre de Wifi: ")
                self.password_wifi = input("Contraseña Wifi: ")
                programa.talk("\nEncendiendo zona wifi...")
                #os.system("cd / ")
                os.system("netsh wlan set hostednetwork mode=allow ssid=" + self.nombre_wifi + " key=" + self.password_wifi)
                os.system("netsh wlan start hostednetwork")
                self.encendido=True
                programa.talk("Se ha encendido la zona wifi correctamente")
            except:
                programa.talk("Error inesperado. Cancelando proceso")
            
                
    
    def apagar_wifi(self):
        if self.encendido==True:
            try:
                programa.talk("\nApagando zona wifi...")
                os.system("netsh wlan stop hostednetwork")
                self.encendido = False
                programa.talk("Se ha apagado la zona wifi")
            except:
                programa.talk("Ocurrio un error mientras se intentaba apagar la zona wifi")
            finally:
                programa.talk("\nSe ha terminado la accion")
                
    def Mostrar_Contraseñas_Guardadas(self):
        os.system("netsh wlan show profile")
    
    def abrir_web(self):
        self.web = webbrowser.open("index.html")
        programa.menu_opciones()
    
    def buscar_wikipedia(self):
        print("\nDiga lo que desea buscar")
        self.text_search = input("Buscar: ")
        wp.set_lang("es")
        self.resultado = wp.summary(self.text_search)
        programa.talk(self.resultado)

    def menu_opciones(self):
        # Menu de opciones
        while True:
            print("\n                     .:Menu:.\n 1. Encender zona wifi\n 2. Apagar zona wifi\n 3. Mostrar contraseñas de wifi guardadas\n 4. Arreglar daños en el sistema\n 5. Detener procesos\n 6. Buscar por Wikipedia\n 7. Abir web oficial\n 8. Descargar un video de youtube\n 9. Salir")
            self.date = datetime.datetime.now()
            print()
            print(self.date)
            self.opcion = input("Opcion: ")
            
            # Opciones para que el usuario elija
            if '1' in self.opcion:
                programa.encender_wifi()
            if '2' in self.opcion:
                programa.apagar_wifi()
            if '3' in self.opcion:
                programa.Mostrar_Contraseñas_Guardadas()
            if '4' in self.opcion:
                reparar()
            '''if '5' in self.opcion:
                stoping_process()'''
            if '6' in self.opcion:
                programa.buscar_wikipedia()
            if '7' in self.opcion:
                programa.talk("Abriendo web oficial del programa")
                programa.abrir_web()
                exit(0)
            elif 'clean' in self.opcion:
                os.system("cls")
            elif '8' in self.opcion:
                download()
            elif '9' in self.opcion:
                programa.talk("Saliendo del programa")
                exit()
                
if __name__=='__main__': 
#    template = Template()
    programa = Programa()
 #   template.show_template()
    programa.talk("Sea bienvenido al programa Útiles, programa con varias utilidades para Rey Michel y que incluso esta en mantenimiento todavia. Cualquier duda contactar con Rey Michel")    
    programa.menu_opciones() 
               

