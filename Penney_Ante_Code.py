import time
import random

#Note to self: in final stages of code, give it a personality. Try to learn machine learning from that udacity course, see if you can make this...smarter...
#Perhaps have it analyze player strategy? Or make its decisions more random
usr_score = 0
cmp_score = 0

#First step: very basic. Asks user for their input, uses the basic strategy for highest probability of winning to choose its own
#Initiates the game
print("Hello! Welcome to the Penney Ante Game! \nPick a series of three coin-flip results!\nFirst to 5 wins! \n*Please use lowercase!*")
usr = input()
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
time.sleep(5)

#This next portion is the actual game
#It randomizes the head or tail values corresponding to 1 or 2 and adds them to a list l
#Then, it checks if a sequence of three appears mathcing either the user's or computer's choice
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
    time.sleep(2)
    a = len(l)
    if a >= 3:
        n = c+3
        v = ''.join(l[(n-6):n])
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


    
