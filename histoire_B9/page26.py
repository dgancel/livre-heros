def page26 (gameState: dict)-> int:
    res: int= -2
    print("Vous êtes dans le couloir entre les ailes A, B et C ")
    print("Maintenat, tu dois choisir la prochaine aile à délivrer ")
    print("1 : Aile A  2: Aile B  3: Aile C")   
    choix: str = input("> ")
    if choix == "1":
                    print("Ailes A, c'est parti")
                    res = 13
    elif choix == "2":
                    print("Aile B en avant  ")
                    res = 16
    elif choix == "3":
                        print("Aile C en avant  ")
                        res = 17
    else :
                    print("Choix invalide.")
                    print("Espèce d'imbécile, on a dit 1 ou 2, pas autres choses")
                    res = 26
    return res