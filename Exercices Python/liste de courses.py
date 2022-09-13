import json

chemin = r"C:\Users\33651\Desktop\SQL\courses.json"
with open (chemin,"r") as fichier:
    liste_de_course = json.load(fichier)
    
while True:
  
# choix invalide
    
    liste_de_choix = ["Choisissez une des options suivantes","1: Ajouter un élément à la liste de courses", "2: Retirer un élément de la liste de courses", "3: Afficher les éléments de la liste de courses", "4: Vider la liste de courses"
, "5: Quitter le programme"]
    print(*liste_de_choix, sep= "\n")
    print()
    choix_option = input ("\U0001f449  Votre choix: ")
    if not choix_option.isdigit() or int (choix_option)<= 0 or int(choix_option) > 5:
        print ("Votre choix est invalide")
        print()
# ajouter un élément 
     
    elif int (choix_option) == 1:
        ajout = input("Quel élément vous souhaitez rajouter ?: ")
        print()
        if ajout not in liste_de_course:
            
            liste_de_course.append(ajout)
            with open (chemin, "w") as fichier:
                json.dump(liste_de_course, fichier)
            print ((f"L'élément {ajout} a bien été ajouté la liste!"))
            print()
        else:
            print (f"L'élément {ajout}  est déja dans la liste!")
            print()
#supprimer un élément
         
    elif int (choix_option) ==2:
        retrait = input("Quel élément souhaitez vous retirer? : ")
        print()
        if retrait in liste_de_course:
            liste_de_course.remove(retrait)
            print (f"L'élément {retrait} a bien été retiré de la liste")
            print()
        else:
            print (f"L'élément {retrait} n'existe pas dans la liste!")
            print()
#afficher la liste

    elif int (choix_option) ==3:
        if liste_de_course ==[]:
            print ("Votre ne contient aucun élément!")
            print()
        else:
            for i, element in enumerate(liste_de_course, 1):
                print (i, element, sep=".")
            print()
#vider la liste de courses

    elif int (choix_option) == 4:
        if liste_de_course ==[]:
            print ("Votre liste est déja vide")
            print()
        else:
            liste_de_course.clear()
            with open (chemin, "w") as fichier:
                json.dump(liste_de_course, fichier)
            print ("Votre liste est désormais vide!")
            print()
#quitter le programme
    elif int (choix_option) == 5:
        print ("Merci et à bientot!")
        break
        