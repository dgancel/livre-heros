def page20 (gameState: dict)-> int:
    res: int= -2
    print("Vous êtes dans le couloir")
    print("Maintenat, à toi de choisir entre aile A, B et l'aile D")
    print("1 : Aile A  2: Aile B 3:Aile C")   
    choix: str = input("> ")
    if choix == "1":
                    print("Aile A, c'est parti")
                    res = 13
    elif choix == "2":
                    print("Aile B en avant toute ")
                    res = 16

    elif choix == "3":
                    print("Aile C en avant !!!!")
                    res=17
    else :
                    print("Choix invalide.")
                    print("Espèce d'imbécile, on a dit 1 ou 2 ou 3, pas autres choses")
                    res = 20
    return res