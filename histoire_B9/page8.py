from random import *
def page8(gameState: dict)-> int:
    res :int = -2
    print("Vous avez rendez vous avec votre référent stage \n Il vous demande comment allez vous en trouver un ?")
    print ("1-Jobteaser 2- Reseau IMT 3-3 Papa/Maman 4- one life go toquer à la porte")
    prob: float = random()
    choix: str= input(">")
    if choix == 1:
        if prob >= 0.40:
            print("Il vous félicite et vous laisse partir")
        else:
            print("Vous avez rien trouvé vous vous faites tuer (-3PV)")
            gameState["vie"] -=3
        res = 19
    elif choix == 2:
        if prob >= 0.30:
            print("Il vous félicite et vous laisse partir")
        else:
            print("Vous avez rien trouvé vous vous faites tuer (-3PV)")
            gameState["vie"] -=3
        res = 19
    elif choix == 3:
        if prob >= 0.10:
            print("Il vous félicite et vous laisse partir")
        else:
            print("Vous avez rien trouvé vous vous faites tuer (-3PV)")
            gameState["vie"] -=3
        res = 19
    elif choix == 4:
        if prob >= 0.80:
            print("Il vous félicite et vous laisse partir")
        else:
            print("Vous avez rien trouvé vous vous faites tuer (-3PV)")
            gameState["vie"] -=3
        res = 19
    else:
        print("choix invalide")
    return res
            