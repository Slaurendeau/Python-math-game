score = 0
for i in range(5):    
    import random
    x = random.randrange(1,10,1)
    y = random.randrange(1,10,1)
    an = input("Want to play? yes or no: ")
    if an == "yes":
        print("good")
        print("Lets do some math practice. Type STOP to stop")

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
        
        elif(an == "Stop"):
            print ("GAME OVER")
            
        else:
            print ("Nope it was")
            print (z)
print("Game over, your score was")
print (score)
print ("/5")