import random
choice = random.randint(1 , 100)
tries =0
guess = -50
while guess != choice:
    guess = int(input("enter a guess between 1 and 100 here:"))
    if guess < choice:
        print("too low try again!")
    elif guess > choice :
        print("too high!")
    m = tries
    tries +=1

print("hey you won!")
print("it took you " + str(m))
