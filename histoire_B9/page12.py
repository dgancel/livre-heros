from random import *
def page12 (gameState: dict)-> int
    res: int = -2
    print("Vous voilà en amphi Chappe. Un QCM est annoncé")
    print("Vous devez entrer votre code de QCM mais vous l'avez oublié !!! Pour vous en sortir vous devez répondre à ces 3 question")
    print("1- f(x) = 2x+4 CALCULER L'INTEGRALE de 0 à 1 \n 2- Comment annuler un ln ? (LA LETTRE) \n 3- La dérivée de arctan(x)")
    rep:str =input("réponse>")
    prob: int = randint (0 , 3)
    if rép == "5e1/1-x**2":
        print ("bravo vous avez réussi")
    else:
        print("Vous avez raté vous tappez votre identifiant au hasard")
        if prob >= 1:
            print ("Par chance vous avez trouvé le bon")
        else:
            print("Vous vous faites défoncer par les profs de maths et vos camarades car à cause de vous la correction a duré 1 semaine")
    res = 9
    return res
        
    
     