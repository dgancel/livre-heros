# Ne pas hésiter à ajouter un random pour embellir
def page10 (gameState: dict)-> int:
    res: int = -2
    print("Vous voici en Morse, vous voyez des sièges très confortables donc vous décidez de vous assoir dessus")
    print("Après un bon repos vous vous sentez mieux")
    gameState["vie"]+=3
    res = 9
    return res