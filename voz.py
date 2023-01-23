import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


name = 'Alice'

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    try:
        with sr.Microphone() as source:
            print("Escuchando....")
            voice = listener.listen(source)
            rec = listener.recognize_google(voice, language='es-ES')
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name, "")
                #talk(rec)
    except:
        pass
    return rec
    
def run():
    rec = listen()
    if 'reproduce' in rec or 'play' in rec:
        music = rec.replace('reproduce', '')
        talk("Reproduciendo " + music) 
        pywhatkit.playonyt(music)
    if 'hora' in rec or 'time' in rec:
        date = datetime.datetime.now().strftime('%H:%M')
        talk("Son las "+date)
    if 'busca ' in rec or 'what is' in rec:
        order = rec.replace('busca', '')
        info = wikipedia.summary(order, 1)
        talk(info)    
run()