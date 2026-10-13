import random
class spelare:
    def __init__(self ,namn ="" ,level="" ,hp="" ,atack=""):
        self.namn =namn
        self.hp=hp*level
        self.level=level
        self.atack=atack*level

class monster:
    def __init__(self,hp,atack,level):
        self.level=level
        self.hp=level*hp
        self.atack=level*atack
class trol(monster):
    def atack(self):
        print("bonk")
class goblin(monster):
    def atack(self):
        print("slash")
class spindel(monster):
    def atack(self):
        print("bite")    
class drake(monster):
    def atack(self):
        print("fire")


class lote:
    def __init__(self,money,special):
        self.__money=money
        self.special=special
class minic:
    def __init__(self,hp,atack,level,  treshur= lote):
        self.treshur=treshur
        super().__init__(hp,atack,level)

trol=trol(10,5,3)
goblin=goblin(10,5,1)
spindel=spindel(10,5,1)
drake=drake(10,5,1)

spelare_namn=input("vad hetter spelare :")
hjälte = spelare(spelare_namn,1,10,5)

map [[ 1, 2, 3, 4, 5]
     [ 6, 7, 8, 9,10]
     [11,12,13,14,15]
     [16,17,18,19,20]
     [21,22,23,24,25]]

game=True
while game==True:
    print("="*30)
    print("        DUNGEON BATTLE")
    print("="*30)
    print(" ")
    print(spelare_namn)
    print("level",(hjälte.level))
    print("hp",(hjälte.hp))
    print("atack",(hjälte.atack))
    print("")

    print("1. gå framåt")
    print("2. gå höger")
    print("3. gå vänster")
    print("4. map")
    print("5.stats")
    val=input("vad vill du göra")

            

    game=False

#    print("1. gå framåt")
#    print("2. gå höger")
#    print("3. gå vänster")

#    val=input("vad vill du göra")
#    if val ==("1"):
#        påträf=random(1,3)
#        if påträf==1:
            
