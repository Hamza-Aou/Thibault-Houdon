#Jeux de rôles
import random

mes_vies, vies_ennemi = 50, 50
potions = 3

print ("Salut Chef! Tu as 50 \U0001f496 et tu disposes de 3 \U0001F9EA")
while mes_vies > 0 and vies_ennemi > 0:
    mon_attaque = random.randint(5, 10)
    attaque_ennemi = random.randint(5, 15)
    choix_attaque = input("Attaque (1) \u2694\uFE0F ou potion (2) \U0001F9EA Chef ? : ")
    print ("\u2B50"*19)

    if choix_attaque.isdigit() and int(choix_attaque) == 1:
        vies_ennemi = vies_ennemi - mon_attaque
        mes_vies = mes_vies - attaque_ennemi
        print (f"Tu lui a infligé {mon_attaque} \u2694\uFE0F")
        print (f"Il t'a infligé {attaque_ennemi} \u2694\uFE0F")
        print (f"Il te reste {mes_vies} \U0001f496")
        print (f"Il lui reste {vies_ennemi} \U0001f496")

        if mes_vies <= 0:
            print ("\U0001f635\u200D\U0001f4ab Tu as perdu \U0001f635\u200D\U0001f4ab")
            break
        if vies_ennemi <= 0:
            print ("\U0001f3c5 \U0001f3c6 Tu as gagné \U0001f3c6 \U0001f3c5")
            break
    if choix_attaque.isdigit() and int(choix_attaque) == 2 and potions > 0:
        potions -= 1
        attaque_ennemi_2 = random.randint(5, 15)
        mes_vies_potion = random.randint(15, 50)
        mes_vies = mes_vies + mes_vies_potion - attaque_ennemi - attaque_ennemi_2
        print (f"Il te reste {potions} potions \U0001f975")
        print (f"Tu as récupéré {mes_vies_potion } \U0001f496 ")
        print (f"Il t'a infligé {attaque_ennemi} \u2694\uFE0F")
        print (f"Il te reste {mes_vies + attaque_ennemi_2 } \U0001f496")
        print (f"Il lui reste {vies_ennemi} \U0001f496")
        print ("\u26A1"*10)
        print ("Tu passes ton tour...")
        print (f"Il t'a infligé {attaque_ennemi_2}\u2694\uFE0F")
        print (f"Il te reste {mes_vies} \U0001f496")
        print (f"Il lui reste {vies_ennemi} \U0001f496")       
    else:
        print ("Hélas! Tu as plus de potions \U0001f915")
    continue