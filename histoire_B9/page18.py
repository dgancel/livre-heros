def page18 (gameState: dict)-> int:
    res: int= -2
    print("Vous êtes dans le couloir")
    print("Maintenat, jeune druide, à toi de choisir entre aile F et l'aile D")
    print("1 : Aile F  2: Aile D")   
    choix: str = input("> ")
    if choix == "1":
                print("Aile F, c'est parti")
                res = 9
    elif choix == "2":
                print("Aile D en avant toute ")
                res = 8
    else :
                print("Choix invalide.")
                print("Espèce d'imbécile, on a dit 1 ou 2, pas autres choses")
                res = 18
    return res