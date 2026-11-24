def page21 (gameState: dict)-> int:
    res: int= -2
    res: int= -2
    print("Vous êtes encore dans le couloir")
    print("Maintenat, vous devez choisir entre aile E  et l'aile  D")
    print("1 : Aile E  2: Aile D")   
    choix: str = input("> ")
    if choix == "1":
                    print("Aile E, c'est parti")
                    res = 5
    elif choix == "2":
                    print("Aile D en avant toute ")
                    res = 8
    else :
                    print("Choix invalide.")
                    print("Espèce d'imbécile, on a dit 1 ou 2, pas autres choses")
                    res = 21
    return res