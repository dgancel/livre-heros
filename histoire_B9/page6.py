def page6 (gameState: list)-> int:
    res: int = -2
    clear: bool = False
    print("Vous voici en amphi Pascal un cours de compta se déroule")
    while not clear == True:
        print("Votre corps commence à s'endormir vous devez trouver un moyen de rester éveillé")
        choix:str= input("Combien prenez vous de cafés ?")
        if choix >= "7":
            print("C'est beaucoup mais assez pour tenir")
            clear = True
        else:
            print("PLUS VOUS SOMNOLEZ DEJA")
            gameState["vie"]-=1
    res = 5
    return res