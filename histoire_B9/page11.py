def page11 (gameState: dict)-> int:
    res: int= -2
    print("Vous êtes maintenant dans l'amphi Shannon, vous ne le connaissez pas, c'est normal c'est l'amphi des CP2")
    print("Qui dit amphi des CP2, dit pour délivrer l'amphi, une question de CP2 :) ")
    print("Petite question d'atomistisque :)")
    print("Pour l’orbitale atomique 3Pz d’un atome hydrogénoïde, combien existe-t-il de surfaces nodales (planes et sphériques confondues) ?")
    print("1: 2 surfaces nodales (1 plan nodal et 1 sphère nodale) 2:  3 surfaces nodales (1 plan nodal et 2 sphères nodales). 3: 2 surfaces nodales (2 plans nodaux et 0 sphère nodale) ")
    choix: str = input("> ")
    if choix == "1":
            print("Bon réponse, tu as l'aura pour un CP2 précoce")
            gameState["vie"]+=1
            res=16
    elif choix == "2":
            print("Dommage mauvaise réponse")
            gameState["vie"]-=1
            res=9
    elif choix =="3":
            print("Dommage mauvaise réponse")
            gameState["vie"]-=1
            res=9
    
    else : 
            print("Choix invalide.")
            print("Espèce d'imbécile, on a dit 1 ou 2 OU 3, pas autres choses")
            res = 11
    
    return res