import random

roll = random.randint(1,6)
guess = int(input("Guess the number between 1-6:"))
if guess == roll :
    print("Correct Number! They rolled a " + str(roll))
else :
    print("Wrong Number! They rolled a " + str(roll))