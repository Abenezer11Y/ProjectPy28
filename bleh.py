import random
playing = True
number = str(random.randint(1, 10))
amt = 1

print("Guess a number between 1 to 10(And you have to guess one at a time).")
print("The game ends when you guess correct.")

while playing:
    guess = input("Enter your guess here: ")
    if number == guess:
        print(f"You Win! It took you {amt} guesses to get it.")
    else:
        print("Wrong. Try again.")
        amt += 1