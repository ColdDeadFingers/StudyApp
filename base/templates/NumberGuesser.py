import random

Guess_Number = random.randint(10, 99)

User_Guess = input("Number has been generated. Enter your guess: ")

Guess_Count = 1

Correct = False

while not Correct:
    if int(User_Guess) > Guess_Number:
        print("You're too high, the number is a lower value")
    elif int(User_Guess) < Guess_Number:
        print("You're too low, the number is a higher value")
    elif int(User_Guess) == Guess_Number:
        print("You win! You guessed the number correctly. It took you " + str(Guess_Count) + " tries")
        Correct = True
        break

    User_Guess = input("Enter new guess: ")
    Guess_Count += 1

print(Guess_Number)