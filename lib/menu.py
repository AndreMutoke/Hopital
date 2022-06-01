from lib.clean import cleanConsonle

def menu():
    cleanConsonle()
    print("###   ### ######### ######### ### ######### ######### ###      ")
    print("###   ### ######### ######### ### ######### ######### ###      ")
    print("###   ### ###   ### ###   ### ###    ###    ###   ### ###      ")
    print("######### ###   ### ######### ###    ###    ######### ###      ")
    print("######### ###   ### ######### ###    ###    ######### ###      ")
    print("###   ### ###   ### ###       ###    ###    ###   ### ###      ")
    print("###   ### ######### ###       ###    ###    ###   ### #########")
    print("###   ### ######### ###       ###    ###    ###   ### #########")

    print("\n\
           1. ENREGISTRER UN DOCTEUR\n\
           2. ENREGISTRER UN PATIENT\n\
           3. GENERER NUMERO DOSSIER\n\
           4. CHERCHER UN PATIENT PAR SES IDENTIFIANTS\n\
           5. CHERCHER UN PATIENT PAR NUMERO DOSSIER\n\
           6. AFFICHER TOUT LES PATIENTS\n\
           7. AFFICHER TOUS LES DOCTEURS\n\
           8. ENREGISTRER LES PLAINTES D'UN PATIENT\n\
           9. ENREGISTRER L'HORAIRE DE CHAQUE DOCTEUR\n\
           10. VERIFIER LA DISPONIBILITE D'UN DOCTEUR\n\
           11. AFFICHER LES PLAINTES D'UN PATIENT\n\
           12. AFFICHER L'IMC D'UN PATIENT SUIVANT SON NUMERO DOSSIER\n\
           0. QUITTER\n")
    choix_menu = int(input(">> "))
    while(choix_menu<0 or choix_menu>12):
        cleanConsonle()
        print("\n\
               1. ENREGISTRER UN DOCTEUR\n\
               2. ENREGISTRER UN PATIENT\n\
               3. GENERER NUMERO DOSSIER\n\
               4. CHERCHER UN PATIENT PAR SES IDENTIFIANTS\n\
               5. CHERCHER UN PATIENT PAR NUMERO DOSSIER\n\
               6. AFFICHER TOUT LES PATIENTS\n\
               7. AFFICHER TOUS LES DOCTEURS\n\
               8. ENREGISTRER LES PLAINTES D'UN PATIENT\n\
               9. ENREGISTRER L'HORAIRE DE CHAQUE DOCTEUR\n\
               10. VERIFIER LA DISPONIBILITE D'UN DOCTEUR\n\
               11. AFFICHER LES PLAINTES D'UN PATIENT\n\
               12. AFFICHER L'IMC D'UN PATIENT SUIVANT SON NUMERO DOSSIER\n\
               0. QUITTER\n")
        choix_menu = int(input(">> "))
    return choix_menu   
