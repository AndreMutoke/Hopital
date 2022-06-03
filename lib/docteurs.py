from lib.clean import*
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
        print("No saved doctors !!!")
