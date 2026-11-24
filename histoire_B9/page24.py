def page24 (gameState: dict)-> int:
    res: int= -2
    res: int= -2
    print("Vous êtes dans le couloir")
    print("Maintenant,tu dois choisir entre aile A et l'aile C")
        print("1 : Aile A  2: Aile C")   
        choix: str = input("> ")
        if choix == "1":
                    print("Aile A, c'est parti")
                    res = 13
        elif choix == "2":
                    print("Aile C en avant toute ")
                    res = 17
        else :
                    print("Choix invalide.")
                    print("Espèce d'imbécile, on a dit 1 ou 2, pas autres choses")
                    res = 24
    return res