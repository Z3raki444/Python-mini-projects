import random  # Importing the random module to generate random numbers

# Function to handle the gameplay
def play_game():
    # Generate a random number between 1 and 100
    answer = random.randint(1, 100)
    chance = 0  # Initialize the chance counter

    # Loop to allow the user up to 5 chances to guess the number
    while chance < 5:
        try:
            # Prompt the user to input their guess
            guess = int(input("Guess a number between 1 to 100: "))
        except ValueError:
            # Handle invalid inputs that are not integers
            print("Invalid input. Please enter a number.")
            continue  # Skip the rest of the loop and ask for input again

        # Check if the guess matches the answer
        if guess == answer:
            print("Congratulations! You won!")
            break  # Exit the loop if the user guesses correctly
        elif guess < answer:
            print("You are low, go higher!")  # Hint to the user if the guess is too low
        else:
            print("You are high, go lower!")  # Hint to the user if the guess is too high

        # Increment the chance counter after each guess
        chance += 1

    # If all chances are used up and the user didn't guess correctly
    if chance == 5 and guess != answer:
        print(f"Game over! The number was: {answer}")

    # Ask the user if they want to play again after the game ends
    try_again = input("Do you want to play again? (y/n): ").strip().lower()
    if try_again == 'y':
        play_game()  # Restart the game if the user chooses 'y'
    else:
        print("Thank you for playing!")  # Exit the game with a farewell message

# Start the game by calling the function
play_game()