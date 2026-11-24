def page17 (gameState: dict)-> int:
    res: int= -2
    print("Vous êtes en salle des serveurs de l'IMT")
    print("Pour délivrer cette salle vous devez répondre à cette question : ")
    print("i = 5 \n  while i < 5: \n  print("Bonjour") \n  i += 1")
    print("Quel est la réponse ?")
    print("1: une infinité de fois 2: 1 fois 2: 0 fois")
    choix: str = input("> ")
    if choix == "1":
        print("Dommage mauvaise réponse")
        gameState["vie"]-=1
        res=24
    elif choix == "2":
        print("Dommage mauvaise réponse")
        gameState["vie"]-=1
        res=24
    elif choix =="3":
        print("Bonne réponse, petit génie de l'informatique, tu prends le controle de My Services petit coquin")
        gameState["vie"]+=1
        res=24

    else : 
        print("Choix invalide.")
        print("Espèce d'imbécile, on a dit 1 ou 2 OU 3, pas autres choses")
        res = 17

    return res