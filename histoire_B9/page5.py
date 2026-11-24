def page5 (gameState: dict)-> int:
    res: int= -2
    print("Vous êtes dans l'aile E :")
    print("Pour commencer à libérer l'IMT, tu dois choisir la salle à délivrer en premier")
    print("1: Amphi Pascal. 2 : Bibliothèque")
    choix: str = input("> ")

    if choix == "1":
        res=6
    elif choix == "2":
        res=7
    else :
        print("Choix invalide.")
        print("Espèce d'imbécile, on a dit 1 ou 2, pas autres choses")
        res = 5                 # on reste sur cette page
    return res