#1 Over Cricket Game with 1 wicket
import random
Batsman1=str(input("Enter first Batsman Name:"))
Batsman2=str(input("Enter second batsman Name: "))
runbatting=0
runchassing=0

ball=0
while ball<=6:
    bowl=input("Enter to Bowl:")
    if bowl=="":
        rand=random.randint(0,7)
        if rand==0:
            ball+=1
            print(rand)
            print("Score",runbatting)
        elif rand>=1 and rand<=6:
            runbatting+=rand
            print(rand)
            print("score",runbatting)
            ball+=1
        elif rand>6:
            ball+=1
            print("Wicket")
            print("played",ball,"Balls")
            break

print("Totall score of batsman1 is",runbatting)
        
ball=0
print("Second Batting")
while ball<=6:
    bowl=input("Enter to Bowl:")
    if bowl=="":
        rand=random.randint(0,7)
        if rand==0:
            ball+=1
            print(rand)
            print("Score",runchassing)
        elif rand>=1 and rand<=6:
            runchassing+=rand
            print(rand)
            print("score",runchassing)
            ball+=1
        elif rand>6:
            ball+=1
            print("Wicket")
            print("played",ball,"Balls")
            break
print("Totall score of batsman2 is",runchassing) 

if runbatting==runchassing:
    print(runbatting,runchassing,"Match is Draw")
elif runbatting>runchassing:
    print(Batsman1," is won")
elif runbatting<runchassing:
    print(Batsman2," is won")
    
    

