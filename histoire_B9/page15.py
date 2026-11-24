def page15 (gameState: dict)-> int:
    res: int= -2
    print("Vous êtes dans la salle de TP elec")
    print("Il est temps de répondre à l'unique question de votre TP représentant 3/4 de votre note finale")
    print("Une batterie de 12V alimente en série $R_1 = 4 ohms, suivie de deux branches parallèles : \n $R_2 = 6 ohms et $R_3 = 12 ohms. \n  Un cavalier métallique relie directement les deux bornes de $R_3$. \n Quelle est la tension aux bornes de $R_2$ ?")
    print("Il se passe quoi")
    print("1 : Tu fais le montage  2: Tu ne fais pas le montage  3: La réponse D(c'est ton binome qui le fait)")   
    choix: str = input("> ")
    if choix == "1":
                    print(" Sale fou, tu viens de mettre le feu au labo ")
                    res = 23
                    gameState["vie"]-=1
    elif choix == "2":
                    print(" Tu as détecté le problème bravo")
                    gameState["vie"]+=1
                    res = 23
    elif choix == "3":
                    print(" Sale fou, tu viens de mettre le feu au labo et c'est quand même de ta faute")
                    gameState["vie"]-=1
    else :
                    print("Choix invalide.")
                    print("Espèce d'imbécile, on a dit 1 ou 2 OU 3, pas autres choses")
                    res = 15
   
    return res