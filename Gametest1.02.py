import time
score = 0

def tell_score():
    print("your score is:")
    print(score)


for i in range(2):    
    import random
    x = random.randrange(1,10,1)
    y = random.randrange(1,10,1)
    an = input("Want to play? yes or no: ")
    if an == "yes":
        print("good")
        print("Lets do some math practice. Type STOP to stop")
        print("Press 0 to check your score")
        print("Press -1 to record score")

    print (x)
    print (y)
    z = (x+y)
    usin = input("what is the sum of these two numbers?")
    
    if(usin == "STOP"):
        print("the game is over!")
        print("your score was")
        print (score)
        
    else: 
        var = int(usin)
    
        if (var == z):
                print ("good job!")
                score = score+1
                print ("your score is")
                print (score)
        
        elif(an == "STOP"):
            print ("GAME OVER")
            
        elif(var == 0):
            tell_score()
            
        else:
            print ("Nope it was")
            print (z)
            score = 0 
print("Game over, your score was")
print (score)
print ("/5")

high = str(score)

file = open("Text.txt", "w")
file.write (high)
file.close()