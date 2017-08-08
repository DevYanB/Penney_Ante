import time
import random

#This is a code inspired by the Penney Ante Logic and Chance Game! Time.sleep's are included for dramatic effect!
usr_score = 0
cmp_score = 0

#First section asks user for their input, uses the basic strategy for highest probability of winning to choose its own;
#Based on non-transitive probability tree of this game(check online), if user gives ABC, optimal result is (!B)AB;
#Makes sure string input is valid;
#Initiates the game.
print("Hello! Welcome to the Penney Ante Game! \nPick a series of three coin-flip results!\nFirst to 5 wins! \n*Please use lowercase!*")
while True:
    usr = input()
    if((len(usr) < 3) or (len(usr) > 3)):
       print("Enter a valid sequence")
       continue;
    else:
       break

mid = usr[1:2]
if mid == 't':
    cmp = 'h' + usr[0:2]
elif mid == 'h':
    cmp = 't' + usr[0:2]
print("Alright, good choice!")

time.sleep (2)
print("I choose: " + cmp)
time.sleep(2)
print("Now, let us play!")
print("")
time.sleep(3)

#This next portion is the actual game;
#It randomizes the head or tail values corresponding to 1 or 2 and adds them to a list l;
#Then, it checks if a sequence of three appears mathcing either the user's or computer's choice;
#If it does, it will add a point to the respective party and start flipping again!

l = []
c = 0

while(c <= 10000):
    c += 1
    x = random.randint(1,2)
    if x == 1:
        l.append('h')
    else:
        l.append('t')
    print(l)
    time.sleep(1)
    if len(l) >= 3:
        n = c-3
        v = ''.join(l[n:(n+3)]) #This function here creates a string of the last 3 terms(once 3 or more terms long) from the array l
                                #and adds spaces between them for comparison to the user inputted string;
                                #Can also just use basic string and concatenation without spaces, but important fact is that it uses 3 most recent terms;
                                #Subtracting 3 from c, setting it as n, then getting substring from n to n+3. works well i think.
        if v == usr:
            usr_score += 1
            l.clear()
            print("\nOne for you...\n")
            time.sleep(2)
            c = 0
        elif v == cmp:
            cmp_score += 1
            l.clear()
            print("\nOne for me!!!\n")
            time.sleep(2)
            c = 0
    if cmp_score == 5:
        print("I win!!!")
        print ("\nUser Score: " + str(usr_score))
        break
    elif usr_score == 5:
        print("You win...")
        print("\nComputer Score: " + str(cmp_score))
        break


    
