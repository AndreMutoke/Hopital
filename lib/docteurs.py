from lib.clean import*
jours = ["lundi",
         "mardi",
         "mercredi",
         "jeudi",
         "vendredi",
         "samedi",
         "dimanche"]
heuresTravail = [ "08h - 09h",
                  "09h - 10h",
                  "10h - 11h",
                  "11h - 12h",
                  "12h - 13h",
                  "13h - 14h",
                  "14h - 15h",
                  "15h - 16h",
                  "16h - 17h"]
def enregistrer_docteur():
    cleanConsonle()
    print("#####################################")
    print("##      ENREGISTRER UN DOCTEUR     ##")
    print("#####################################")
    
    liste = []    
    print("Entrez le prenom du docteur")
    prenom = input(">> ")
    prenom = prenom.upper()
    liste.append(prenom)
    print("Entrez le nom du docteur")
    nom = input(">> ")
    nom = nom.upper()
    liste.append(nom)
    print("Entrez le post_nom du docteur")
    post_nom = input(">> ")
    post_nom = post_nom.upper()
    liste.append(post_nom)
    print("Entrez le telephone du docteur")
    telephone = input(">> ")
    liste.append(telephone)
    print("Entrez le matricule du docteur")
    matricule = input(">> ")
    liste.append(matricule)
    print("Entrez la specialite du docteur")
    specialite = input(">> ")
    specialite = specialite.upper()
    liste.append(specialite)
    return liste
    
def afficher_docteur(docteurs):
    cleanConsonle()
    print("#####################################")
    print("##        LISTE DES DOCTEURS       ##")
    print("#####################################")
    #verification des docteurs enregistres
    if len(docteurs) != 0:
        for i in range(len(docteurs)):
            print(f"\n\
            Prenom : {docteurs[i][0]}\n\
            Nom : {docteurs[i][1]}\n\
            Post-nom : {docteurs[i][2]}\n\
            Numero Telephone: {docteurs[i][3]}\n\
            Matricule : {docteurs[i][4]}\n\
            Specialite: {docteurs[i][5]}\n")
    else:
        print("Pas des docteurs enregistrer pour l'instant !!!\n")
def enregistrer_horaire(docteur):
    cleanConsonle()
    horaire = []
    print(f"Docteur : {docteur[0]} {docteur[1]} {docteur[2]}")
    print("-------------------------------------------------")
    for i in range(len(jours)) :
        programmeHeure = []
        for j in range(len(heuresTravail)) :
            print(f"Entrez l'horaire du {jours[i]} de {heuresTravail[j]} :")
            prog = input(">> ")
            prog = prog.upper()
            programmeHeure.append(prog)
        horaire.append(programmeHeure)
    docteur.append(horaire)
def afficher_horaire(docteur):
    if len(docteur) <= 6 :
        print("Desole il n'ya pas d'horaire pour l'instant")
    else :
        print(f"Docteur : {docteur[0]} {docteur[1]} {docteur[2]}")
        print("-------------------------------------------------") 
        for i in range(len(jours)):
            print(f"{jours[i]} :")
            for j in range(len(heuresTravail)) :
                print(f"\t{heuresTravail[j]} : {docteur[6][i][j]}")




                           
