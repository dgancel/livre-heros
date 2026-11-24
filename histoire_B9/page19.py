def page19 (gameState: dict)-> int:
    res: int= -2
    print("Vous êtes dans le couloir")
    print("Maintenat, tu dois choisir entre aile E et l'aile F")
    print("1 : Aile E  2: Aile F")   
    choix: str = input("> ")
    if choix == "1":
                    print("Aile E, c'est parti")
                    res = 5
    elif choix == "2":
                    print("Aile F en avant toute ")
                    res = 9
    else :
                    print("Choix invalide.")
                    print("Espèce d'imbécile, on a dit 1 ou 2, pas autres choses")
                    res = 19
    return res