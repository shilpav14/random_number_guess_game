import random

process = True
no = random.randint(0,20)
chance = 0
name = input("Hello there! , what's your name? \n")
print("Hello!", name, "I am going to guess a number between 0 and 20.\n")
print("Let's see if you can guess the number in the 5 guess that I give you\n")
while process == True:
    choice = input("Guess a number")
    if int(choice) == no:
        print("Well done!! You guessed it.")
        print("Would you like to play again", name, "?", "\n 1. Yes \n 2.No")
        option = input()
        if option == str(1):
            choice = 0
            pass
        if option == str(2):
            exit("Thank you for playing......")
    elif int(choice) > no:
        print("Your number is too high")
        chance = chance + 1
    elif int(choice) < no:
        print("Your number is too small")
        chance = chance + 1
    else:
        pass

    if int(chance) == 5:
        print("You have reached the maximum number of chances\n")
        print("The number I was thinking of was", no)
        exit()

