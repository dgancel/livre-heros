def page14 (gameState: dict)-> int:
    res: int= -2
    print("Vous êtes en cours de langue : ")
    print("Hello everyone, welcome to this english class")
    print("A little question, to start the lesson")
    print("Which sentence is grammatically idiomatic and natural in formal English?")
    print(" 1: Had the board been apprised of the liability earlier, they might have averted it.")
    print("2: Had the board been apprised of the liability earlier, it might have been averted.")
    print("3: Were the board apprised of the liability earlier, it might have been averted.")
    choix: str = input("> ")
    if choix == "1":
                print("Bad mood")
                gameState["vie"]-=1
                res=13
    elif choix == "2":
                print("Good job")
                gameState["vie"]+=1
                res=13
        elif choix =="3":
                print("bad mood too")
                gameState["vie"]-=1
                res=13
        
        else : 
                print("Choix invalide.")
                print("Espèce d'imbécile, on a dit 1 ou 2 OU 3, pas autres choses")
                res = 14
    return res