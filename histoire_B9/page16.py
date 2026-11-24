def page16 (gameState: dict)-> int:
    res: int = -2
    test: list =[
        [0,1,-1,-1,0,253],
        [0,0,-1,-1,1,412],
        [1,0,-1,0,-1,331],
        ]
    print("Vous trouvez une feuille de turing machine ainsiqu'un exercice au tableau")
    print("Les vérificateurs: \n 1- Ce vérificateur vérifie BLEU la valeur comparée à 3 (>3 <3 =3)\n 2- Ce vérificateur vérifie si les 3 valeurs sont en ordre croissant, décroissant ou aucun des deux ( Croissant/décroissant/rien)")
    print("-3 Ce vérificateur vérifie qu'une couleur spécifique est paire ou impaire ( Bleu est pair / Bleu est impair OU Jaune est pair / Jaune est impair OU Violet est pair / Violet est impair)")
    print("4-Ce vérificateur vérifie quelle couleur a la plus petite valeur (ou plus petite à égalité) (BLEU/JAUNE/VIOLET)")
    print("5- Ce vérificateur vérifie une couleur spécifique comparée à une autre couleur spécifique OUPS UN HACKER A REVELE LA REPONSE (BLEU>JAUNE)")
    print("les tests: \n lexique: 0 pas testé, 1 oui, -1 non, code à la fin")
    for i in range (len(test)):
        print (test[i])
    rep: str = input("votre réponse pas de justification demandée")
    if rep == "325":
        print("bravo vous êtes un GOAT")
        res=24
    else:
        print("Nullos pas capable de comprendre la logique")
        res = -1
    return res