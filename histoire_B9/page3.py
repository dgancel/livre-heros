from OUTILS.aleatoire import *
def page3 (gameState : dict)-> int:
    rep: str = ""
    res: int = -2
    print("Vous avez pris l'entrée cachée à l'arrière de l'école \n Malheureusement, vous avez pas le badge pour entrer donc vous attendez que quelqu'un du BDE vienne vous ouvrir")
    while rep == "" or rep == "non":
        print (annonce (2,3))
        rep =input("prêt ? (écrire non pour attendre)")
    print("votre nombre", start(2,3))
    prob: int = start(2,3)
    if prob < 3:
        print("Après quelques minutes quelqu'un vous ouvre")
        res = 5
    else:
        print("Personne ne vous a ouvert alors vous décidez de prendre l'entrée principale")
        res = 2
    return res