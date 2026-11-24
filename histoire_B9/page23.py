def page23 (gameState: dict)-> int:
    res: int= -2
    print("Vous êtes dans le couloir entre les ailes B et C")
    print("MaintenaNT à toi de choisir ")
    print("1 : Aile B  2: Aile C")   
    choix: str = input("> ")
    if choix == "1":
                    print("Aile B, c'est parti")
                    res = 16
    elif choix == "2":
                    print("Aile C, let's go ")
                    res = 17
    else :
                    print("Choix invalide.")
                    print("Espèce d'imbécile, on a dit 1 ou 2, pas autres choses")
                    res = 23
    return res