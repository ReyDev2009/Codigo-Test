# Crear un diccionario con preguntas y respuestas
import os

import pyttsx3

class Program:
    def __init__(self):
        self.preguntas_respuestas = {
        "Cuál es el planeta más grande del sistema solar?": "Júpiter",
        "Cuál es el país con mayor población?": "China",
        "Cuál es el río más largo del mundo?": "El Nilo",
        "Mejor jugador de futbol nacido en Portugal?": "Cristiano Ronaldo"
    }
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[2].id)
        
    def talk(self, text):
        self.engine.say(text)
        self.engine.runAndWait()
       



   
    # Preguntar al usuario
    def question(self):
        programa.talk("Ingrese una pregunta")
        self.pregunta = input("Ingresa una pregunta: ")

        # Obtener respuesta utilizando el método get()
        if self.pregunta != "":
            try:
                self.respuesta = self.preguntas_respuestas.get(self.pregunta)
                if self.respuesta == None:
                    print("Lo siento, no tengo la respuesta para esa pregunta")
                # Mostrar respuesta
                else:
                    print(self.respuesta)
            except TypeError as e:
                print("Error en el sistema...: " + str(e))
        else:
            print("Por favor ingrese una pregunta")
       
programa = Program()    
programa.question()

