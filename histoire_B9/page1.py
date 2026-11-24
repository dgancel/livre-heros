def page1(gameState: dict) -> int:
    res: int = -2                     # par défaut : cas non prévu

    print(f"{gameState['nom']}, vous êtes à l'extérieur de l'IMT.")
    print("Vous devez choisir pr ou entrer dans l'IMT  ?")
    print("1 - Entrée Principale   2 - Entrée BDE")
    choix: str = input("> ")

    if choix == "1":
        print("Vous passez passe à par la grande porte.")
        res = 2
    elif choix == "2":
        print("Vous passez par l'entrée des artisres ;)")
        res = 3
    else:
        print("Choix invalide.")
        print("Espèce d'imbécile, on a dit 1 ou 2, pas autres choses")
        res = 1                  # on reste sur cette page

    return res
