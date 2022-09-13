continuer = "o"
while continuer == "o":
    a = int(input(" Mettez la premiere longueur souhaitee : "))
    b = int(input(" Mettez la deuxième longueur souhaitee : "))
    c = int(input(" Mettez la troisieme longueur souhaitee : "))
    if a+b > c:
        if a == b == c:
            print("Votre triangle existe et c'est un triangle equilateral")
        elif a == b != c:
            print("Votre triangle existe et c'est une triangle isocele")
        elif a**2+b**2 == c**2:
            print("Votre triangle existe et c'est un triangle rectangle")
        else:
            print("Votre triangle existe et c'est un triangle quelconque")
    else:
        print("Votre triangle n'existe pas")
    continuer = input(" souhaitez-vous recommencer ? o/n : ")
