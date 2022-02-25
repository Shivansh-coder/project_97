import random

number = random.randint(1,9)
chances = 0
while chances < 5:
    guess = int(input("Enter your guess"))
    if guess == number:
        print("YOU HAVE WON!!")
        break
    elif guess>number:
        print("Enter a number lower than ")
        
    else:
        print("Enter a number greater than")
    chances = chances + 1

if chances == 5:
    print("You LOOSE:(")