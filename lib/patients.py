from lib.clean import*
import datetime

def affichage_identifiants_patients(patient):
    print(f"\n\
    Nom : {patient[0]} {patient[1]} {patient[2]}\n\
    Numero Telephone: {patient[3]}\n\
    Poids : {patient[4]} Kg\n\
    Taille: {patient[5]} metres\n\
    Genre : {patient[6]}\n\
    Age : {patient[7]} ans\n\
    Numero Dossier: {patient[8]}\n")
def choix_identifiants():
    print("Veuillez choisir votre identifiant : \n\
            1. Nom\n\
            2. Post Nom\n\
            3. Prenom\n")
    identifiant = int(input(">> "))
    while identifiant >3 or identifiant < 1 :
        print("Veuillez choisir votre identifiant : \n\
                1. Nom\n\
                2. Post Nom\n\
                3. Prenom\n")
        identifiant = int(input(">> "))
    if identifiant == 1 :
        print("Entrez le nom du patient : ")
        nom = input(">> ")
        nom = nom.upper()
        return nom
    elif identifiant == 2:
        print("Entrez le post-nom du patient : ")
        post_nom = input(">> ")
        post_nom = post_nom.upper()
        return post_nom
    else :
        print("Entrez le prenom du patient : ")
        prenom = input(">> ")
        prenom = prenom.upper()
        return prenom
def numero_chercher():
    print("Entrez le numero dossier chercher : ")
    num = int(input(">> "))
    return num

def enregistrer_patients():
    cleanConsonle()
    print("#####################################")
    print("##      ENREGISTRER UN PATIENT     ##")
    print("#####################################")
    liste = []
    
    print("Entrez le prenom du patient")
    prenom = input(">> ")
    prenom = prenom.upper()
    liste.append(prenom)
    print("Entrez le nom du patient")
    nom = input(">> ")
    nom = nom.upper()
    liste.append(nom)
    print("Entrez le post-nom du patient")
    post_nom = input(">> ")
    post_nom = post_nom.upper()
    liste.append(post_nom)
    print("Entrez le numero de telephone du patient")
    num = input(">> ")
    liste.append(num)
    print("Entrez le poids du patient en Kg")
    poids = int(input(">> "))
    liste.append(poids)
    print("Entrez la taille du patient en metres")
    taille = float(input(">> "))
    liste.append(taille)
    print("Entrez le genre du patient M/F")
    genre = input(">> ")
    genre = genre.upper()
    while genre != "M" and genre != "F":
        print("Entrez le genre du patient M/F")
        genre = input(">> ")
        genre = genre.upper()
    liste.append(genre)
    print("Entrez l'age du patient")
    age = int(input(">> "))
    liste.append(age)
    current_time = datetime.datetime.now()
    numDossier =current_time.year  + current_time.second
    liste.append(numDossier)
    return liste

def  afficher_patient(patients):
    cleanConsonle()
    print("#####################################")
    print("##        LISTE DES PATIENTS       ##")
    print("#####################################")
    #verification des docteurs enregistres
    if len(patients) != 0:
        for i in range(len(patients)):
            affichage_identifiants_patients(patients[i])
    else:
        print("Pas des patients enregistres pour l'instant !!!\n")
def chercher_patient_identifiant(patients, identifiant):
    if len(patients) != 0:
        for i in range(len(patients)):
            if identifiant == patients[i][0] or identifiant == patients[i][1] or identifiant == patients[i][2] :
                affichage_identifiants_patients(patients[i])
            if identifiant == patients[i][8]:
                affichage_identifiants_patients(patients[i])
                
    else:
        print("Pas des patients enregistres pour l'instant !!!\n")



    
