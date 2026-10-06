
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

trol=monster(10,5,3)

goblin=monster(10,5,1)

spindel=monster(10,5,1)

banditer=monster(10,5,1)

mimic=monster(10,5,1)

drake=monster(10,5,1)

spelare_namn=input("vad hetter spelare :")
hjälte = spelare(spelare_namn,1,10,5)



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



    game=False





#    print("1. gå framåt")
#    print("2. gå höger")
#    print("3. gå vänster")

#    val=input("vad vill du göra")
#    if val ==("1"):
#        påträf=random(1,3)
#        if påträf==1:
            
