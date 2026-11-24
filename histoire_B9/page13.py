def page13 (gameState: dict)-> int:
    res: int= -2
    print("Vous êtes dans l'aile A")
    print("2 choix s'offrent à vous")
    print("1 : Allez en cours d'anglais 2: TP d'élec")   
    choix: str = input("> ")

    if choix == "1":
            print("Let's GO !!!!!!")
            res = 14
    elif choix == "2":
            print("Un TP elec c'est parti ")
            res = 15
    else :
            print("Choix invalide.")
            print("Espèce d'imbécile, on a dit 1 ou 2, pas autres choses")
            res = 13     


    return res