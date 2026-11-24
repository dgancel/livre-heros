def page4 (gameState: dict)-> int:
    res: int= -2
    print("Vous avez pris l'entrée principale")
    print ("Devant vous se trouve 3 ailes:")
    print ("1 Aile D 2-Aile E 3- Aile F")
    choix: str = input(">")
    if choix == "1":
        res = 8
    elif choix == "2":
        res = 5
    elif choix == "3":
        res = 9
    else:
        print("choix invalide OU Aile déjà visitée")
        res = 2
    return res
    
    