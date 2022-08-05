import random
print("Welcome to guessing number game")
number = random.randint(1,31)
def easy(attempts):
    if(attempts>0):
        guess = int(input("Make a guess between 1 and 30 "))
        if(guess == number):
            print("You win!")
        else:
            attempts = attempts - 1
            if(guess>number):
                print("Too high")
                print("Make a guess again")
                print(f"Attempts left is {attempts}")
                easy(attempts)
            else:
                print("Too low")
                print("Make a guess again")
                print(f"Attempts left is {attempts}")
                easy(attempts)
    else:
        print("You are out of guesses")

def hard(attempts):
    if(attempts>0):
        guess = int(input("Make a guess between 1 and 100 "))
        if(guess == number):
            print("You win!")
        else:
            attempts = attempts - 1
            if(guess>number):
                print("Too high")
                print("Make a guess again")
                print(f"Attempts left is {attempts}")
                easy(attempts)
            else:
                print("Too low")
                print("Make a guess again")
                print(f"Attempts left is {attempts}")
                easy(attempts)
    else:
        print("You are out of guesses")

choice = int(input("What do you choose? easy or hard? Type 1 for easy and 2 for hard " ))

if(choice == 1):
    attempts = 10
    print(f"You have {attempts} attempts")
    easy(attempts)
elif(choice == 2):
    attempts = 5
    print(f"You have {attempts} attempts")
    hard(attempts)
    