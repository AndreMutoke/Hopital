from lib.menu import menu
from lib.clean import*
from lib.docteurs import *

#Variables globales
docteurs = []
def gestion_hopital():
    option = menu()
    if option == 0:
        return
    elif option == 1:
        docteurs.append(enregistrer_docteur())
        pauseConsole()
        gestion_hopital()
    elif option == 2:
        print("Option 2")
    elif option == 3:
        print("Option 3")
    elif option == 4:
        print("Option 4")
    elif option == 5:
        print("Option 5")
    elif option == 6:
        print("Option 6")
    elif option == 7:
        afficher_docteur(docteurs)
        pauseConsole()
        gestion_hopital()
    elif option == 8:
        print("Option 8")
    elif option == 9:
        print("Option 9")
    elif option == 10:
        print("Option 10")
    elif option == 11:
        print("Option 11")
    else:
        print("Option 12")
        
        
