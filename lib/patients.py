from lib.clean import*
import datetime

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
    print("Entrez le p0st-nom du patient")
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

def  aficher_patient(patients):
    cleanConsonle()
    print("#####################################")
    print("##        LISTE DES PATIENTS       ##")
    print("#####################################")
    #verification des docteurs enregistres
    if len(patients) != 0:
        for i in range(len(patients)):
            print(f"\n\
            Nom : {patients[i][0]} {patients[i][1]} {patients[i][2]}\n\
            Numero Telephone: {patients[i][3]}\n\
            Poids : {patients[i][4]} Kg\n\
            Taille: {patients[i][5]}\n\
            Genre : {patients[i][6]}\n\
            Age : {patients[i][7]} ans\n\
            Numero Dossier: {patients[i][8]}\n")
            
    else:
        print("No saved patients !!!")





    
