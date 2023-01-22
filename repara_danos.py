import os

def reparar():
    try:
        print("Reparando daños en el sistema esto puede tardar un tiempo")
        os.system("sfc /scannow")
        print("Se ha terminado de arreglar los daños correctamente")
    except:
        print("Error al intentar reparar los daños")
        