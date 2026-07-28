import random

best_score = None  # Stores the fewest guesses needed


def choose_difficulty():
    """Returns the maximum number of guesses based on difficulty."""
    print("\nChoose a difficulty:")
    print("1. Easy (5 guesses)")
    print("2. Medium (4 guesses)")
    print("3. Hard (2 guesses)")

    while True:
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            return 5
        elif choice == "2":
            return 4
        elif choice == "3":
            return 2
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


while True:
    print("Number Guessing Game")

    number = input("Enter a number to set the range: ")

    if number.isdigit():
        number = int(number)

        if number <= 0:
            print("Please type a number greater than 0.")
            continue
    else:
        print("Please enter a valid number.")
        continue

    max_guesses = choose_difficulty()

    random_number = random.randint(0, number)
    guesses = 0

    print(f"\nI'm thinking of a number between 0 and {number}.")
    print(f"You have {max_guesses} guesses.\n")

    while guesses < max_guesses:
        guesses += 1

        user_guess = input(
            f"Guess #{guesses}/{max_guesses}: "
        )

        if not user_guess.isdigit():
            print("Please enter a valid number.\n")
            guesses -= 1  # Don't count invalid input
            continue

        user_guess = int(user_guess)

        if user_guess == random_number:
            print("\nCongratulations! You guessed correctly!")
            print(f"It took you {guesses} guesses.")

            if best_score is None or guesses < best_score:
                best_score = guesses
                print("New Best Score!")

            print(f"Best Score: {best_score} guesses")
            break

        elif user_guess > random_number:
            print("Too high!\n")

        else:
            print("Too low!\n")

    else:
        print("\nYou've run out of guesses!")
        print(f"The correct number was {random_number}.")

    if best_score is not None:
        print(f"\nCurrent Best Score: {best_score} guesses")

    play_again = input("\nWould you like to play again? (y/n): ").lower()

    if play_again != "y":
        print("\nThanks for playing! ")
        break
