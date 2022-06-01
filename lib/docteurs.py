from lib.clean import*
def enregistrer_docteur():
    cleanConsonle()
    print("#####################################")
    print("#####################################")
    print("##      ENREGISTRER UN DOCTEUR     ##")
    print("#####################################")
    print("#####################################")
    
    liste = []
    print("Entrez le prenom du docteur")
    prenom = input(">> ")
    liste.append(prenom)
    print("Entrez le nom du docteur")
    nom = input(">> ")
    liste.append(nom)
    print("Entrez le post_nom du docteur")
    post_nom = input(">> ")
    liste.append(post_nom)
    print("Entrez le telephone du docteur")
    telephone = input(">> ")
    liste.append(telephone)
    print("Entrez le matricule du docteur")
    matricule = input(">> ")
    liste.append(matricule)
    print("Entrez la specialite du docteur")
    specialite = input(">> ")
    liste.append(specialite)
    return liste
    
