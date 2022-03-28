import random

numList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
random = random.choice(numList)

userGuess = int(input("Guess the correct number between 0 to 9 - "))
i = 1
while i > 0:
    if userGuess == random:
        print("You guessed the correct number")
        break
    else: 
        print("wrong number guessed")
        userGuess = int(input("Guess the correct number between 0 to 9 - "))