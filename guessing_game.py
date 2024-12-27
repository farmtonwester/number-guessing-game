import random

secret_number = random.randint(1, 100)
guess_count = 0
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100. Can you guess it?")


while True:
    
    try:
      
        guess = int(input("Enter your guess: "))
        guess_count += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the number!")
            print(f"It took you {guess_count} guesses!")
            break # to exit the loop once the game ends
    except ValueError:
        print("Invalid input. Please enter a number. This guess does not count.")
    