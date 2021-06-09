# snake-water-gun
# snake water ko pee jata ha-winner snake- ----gun water ma doob jaye ge-winner water- ----gun snake ko mar da ge-winner gun-
# radndom.choice module use krna ha
# or computer ko e values da dani han list ma
# or user sa input lani ha
# or program 10 bar chla ga through while loop
# end per jis ka point zyada howa wo jeet jaye ga 

print("Welcome the snake-water-gun game")
import random
def swg():
    atp=0
    com_point=0
    user_point=0
    while (atp<=10):
        lst = ["snake","water","gun"]
        c=random.choice(lst)
        user = int(input("Enter 1 for snake 2 for water and 3 for gun: "))
        if user==1 and c=="snake":
            print(f"you entered the snake and computer also choose the snake.so no points,{atp}")
        elif user==2 and c=="water":    
            print(f"you entered the water annd computer also choose the water. so no point,{atp}")
        elif user==3 and c=="gun":
            print(f"you entered the water annd computer also choose the water. so no point,{atp}")
        elif user==1 and c=="water":
            print(f"snake drink the water and you win,{atp}")
            user_point=user_point+1
        elif user==1 and c=="gun":
            print(f"you lose the game because gun killed the snake,{atp}")
            com_point=user_point+1
        elif user==2 and c=="snake":
            print(f"you lose the game because snake drink the water,{atp}")
            com_point=com_point+1
        elif user==2 and c=="gun":
            print(f"you win the game gun is lost in the water because ,{atp}")
            user_point=user_point+1
        elif user==3 and c=="snake":
            print(f"you win because gun killed the snake,{atp}")
            user_point=user_point+1
        elif user==3 and c=="water":
            print(f"you lose because gun is lost,{atp}")
            com_point=com_point+1
        else:
            print("you enterd valid value")
        atp=atp+1
        if atp==10:
            if user_point>com_point:
                print(f"you win the game successfully and you points is=>{user_point}")
            else:
                print(f"you lose the game unfortunatlly and try again and your points is=>{user_point}")
            again=int(input("if you run again the game please enter 1 and for exit press any key: "))
            if again==1:
                swg()
            else:
                print("Thanks!")
swg()

 