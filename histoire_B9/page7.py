from time import *
def page7 (gameState: dict)-> int:
    res: int = -2
    print("Vous voici dans la bibliothèque,devant vous se trouve un ordinateur et des livres.")
    print("Voulez vous: 1 Faire une recherche avancée 2-Chercher sur un ordinateur")
    choix: str= input (">")
    if choix == "1":
        print("...")
        sleep(2)
        res = 5
    elif choix == "2":
        print("Veuillez patientez recherche en cours: la connexion est lente vous perdez du temps (-5 PV)")
        sleep(20)
        gameState["vie"]= gameState ["vie"] - 5
        res= 5
    else:
        print("Choix impossible vous cassez la réalité") 
    return res
    