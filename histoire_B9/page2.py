from OUTILS.aleatoire import *
from random import * #le nombre se trouve entre 0 et 1
def page2(gameState:dict)-> int:
    rep:str =""
    res: int =-2
    print("Pour entrer veuillez présenter votre badge")
    prob:int = 0
    while rep == "" or rep == "non":
        print (annonce (4,5))
        rep =input("prêt ? (écrire non pour attendre)")
    print("votre nombre", start(1,5))
    prob: int = start(1,5)
    if prob <= 1:
        print("Vous n'avez pas trouvé votre badge. Dommage :/")
        gameState["vie"] = gameState["vie"] - 1
    else:
        print("Vous trouvez votre badge GG")
    res = 4
    return res