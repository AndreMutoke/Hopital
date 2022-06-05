from lib.menu import menu
from lib.clean import *
from lib.docteurs import *
from lib.patients import *

#Variables globales
docteurs = []
patients = []
def gestion_hopital():
    option = menu()
    if option == 0:
        return
    elif option == 1:
        docteurs.append(enregistrer_docteur())
        pauseConsole()
        gestion_hopital()
    elif option == 2:
        patients.append(enregistrer_patients())
        pauseConsole()
        gestion_hopital()
    elif option == 3:
        print("Option 3")
    elif option == 4:
        identifiant = choix_identifiants()
        chercher_patient_identifiant(patients, identifiant, 1)
        pauseConsole()
        gestion_hopital()
    elif option == 5:
        identifiant = numero_chercher()
        chercher_patient_identifiant(patients, identifiant, 1)
        pauseConsole()
        gestion_hopital()
    elif option == 6:
        afficher_patient(patients, 1)
        pauseConsole()
        gestion_hopital()
    elif option == 7:
        afficher_docteur(docteurs)
        pauseConsole()
        gestion_hopital()
    elif option == 8:
        ident = []
        print("Entrez le prenom du patient : ")
        prenom = input(">> ")
        prenom = prenom.upper()
        ident.append(prenom)
        print("Entrez le nom du patient : ")
        nom = input(">> ")
        nom = nom.upper()
        ident.append(nom)
        print("Entrez le post-nom du patient : ")
        post_nom = input(">> ")
        post_nom = post_nom.upper()
        ident.append(post_nom)
        chercher_patient_identifiant(patients, ident, 2)
        pauseConsole()
        gestion_hopital()
    elif option == 9:
        cleanConsonle()
        print("#######################################")
        print("##        HORAIRE DES DOCTEURS       ##")
        print("#######################################")
        for i in range(len(docteurs)):
            enregistrer_horaire(docteurs[i])
        pauseConsole()
        gestion_hopital()
    elif option == 10:
        cleanConsonle()
        print("#############################################")
        print("##        DISPONIBILITE DES DOCTEURS       ##")
        print("#############################################")
        print("\n\
                1. VOIRE HORAIRE DES DOCTEURS\n\
                2. PROGRAMMER UN RENDEZ VOUS\n")
        choix = int(input(">> "))
        while choix != 1 and choix != 2 :
            cleanConsonle()
            print("#############################################")
            print("##        DISPONIBILITE DES DOCTEURS       ##")
            print("#############################################")
            print("\n\
                    1. VOIRE HORAIRE DES DOCTEURS\n\
                    2. PROGRAMMER UN RENDEZ VOUS\n")
            choix = int(input(">> "))
        if choix == 1:
            for i in range(len(docteurs)):
                afficher_horaire(docteurs[i])
        pauseConsole()
        gestion_hopital()
    elif option == 11:
        ident = []
        print("Entrez le prenom du patient : ")
        prenom = input(">> ")
        prenom = prenom.upper()
        ident.append(prenom)
        print("Entrez le nom du patient : ")
        nom = input(">> ")
        nom = nom.upper()
        ident.append(nom)
        print("Entrez le post-nom du patient : ")
        post_nom = input(">> ")
        post_nom = post_nom.upper()
        ident.append(post_nom)
        chercher_patient_identifiant(patients, ident, 3)
        pauseConsole()
        gestion_hopital()
    else:
        print("Option 12")
        
        
