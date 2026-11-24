def page9 (gameState: dict)-> int:
    res: int= -2
    print("Vous êtes dans l'aile F :")
    print("Pour continuer, choisis la salle de  F que tu souhaites délivrer en premier")
    print("1: Amphi Morse  2 : Amphi Shannon 3: Amphi Chappe")
    choix: str = input("> ")

    if choix == "1":
        res=10
    elif choix == "2":
        res=11
    elif choix == "3":
        res = 12
    else :
        print("Choix invalide.")
        print("Espèce d'imbécile, on a dit 1 ou 2 ou 3, pas autres choses")
        res = 9                 # on reste sur cette page
    return res