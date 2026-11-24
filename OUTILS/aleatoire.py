from random import *
def annonce (a: int , b: int)->str:
    res: str = ""
    res = "Vous vous aprétez à réaliser un test de probabilité vous avez ",a ,"chance sur" ,b ,"de réussir"
    return res

def start (a: int, b: int)->int:
    res:int = 0
    res = randint (a,b)
    return res

#def multiple (x: int, a: int, b: int)-> int:
 #  res: int = 0
  # for i in range x:
   #     res+= randint(a,b)
    #return res

