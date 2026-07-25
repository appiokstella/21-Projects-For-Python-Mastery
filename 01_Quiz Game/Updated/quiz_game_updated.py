"""
Quiz School
Main Program - Part 1
"""

import random
from datetime import datetime

from questions import QUESTIONS

# ----------------------------------------
# Files
# ----------------------------------------

PERSONAL_BEST_FILE = "personal_best.txt"
HISTORY_FILE = "quiz_history.txt"


# ----------------------------------------
# Create files if they don't exist
# ----------------------------------------

try:
    with open(PERSONAL_BEST_FILE, "x") as file:
        file.write("0")
except FileExistsError:
    pass

try:
    with open(HISTORY_FILE, "x") as file:
        pass
except FileExistsError:
    pass


# ----------------------------------------
# Personal Best Functions
# ----------------------------------------

def get_personal_best():
    """
    Returns the saved personal best score.
    """

    try:
        with open(PERSONAL_BEST_FILE, "r") as file:
            return int(file.read())

    except:
        return 0


def save_personal_best(score):
    """
    Saves a new personal best.
    """

    with open(PERSONAL_BEST_FILE, "w") as file:
        file.write(str(score))


# ----------------------------------------
# Quiz History
# ----------------------------------------

def save_history(category, difficulty, score, total):
    """
    Saves quiz attempt to history.
    """

    now = datetime.now()

    percentage = (score / total) * 100

    with open(HISTORY_FILE, "a") as file:

        file.write(
            f"{now.strftime('%d/%m/%Y')} | "
            f"{now.strftime('%H:%M:%S')} | "
            f"{category} | "
            f"{difficulty} | "
            f"{score}/{total} | "
            f"{percentage:.1f}%\n"
        )


# ----------------------------------------
# Welcome Screen
# ----------------------------------------

print("=" * 55)
print("🧠 Welcome to Quiz School!")
print("=" * 55)

play = input("Do you want to play? (Yes/No): ").strip().lower()

if play != "yes":
    print("\nThanks for visiting Quiz School!")
    quit()


# ----------------------------------------
# Category Selection
# ----------------------------------------

categories = list(QUESTIONS.keys())

print("\nChoose a Category\n")

for index, category in enumerate(categories, start=1):
    print(f"{index}. {category}")

while True:

    choice = input("\nEnter your choice: ")

    if choice.isdigit():

        choice = int(choice)

        if 1 <= choice <= len(categories):
            break

    print("❌ Invalid choice. Try again.")

selected_category = categories[choice - 1]


# ----------------------------------------
# Difficulty Selection
# ----------------------------------------

print("\nChoose Difficulty\n")

print("1. Easy")
print("2. Medium")
print("3. Hard")

while True:

    difficulty_choice = input("\nEnter your choice: ")

    if difficulty_choice == "1":
        selected_difficulty = "Easy"
        break

    elif difficulty_choice == "2":
        selected_difficulty = "Medium"
        break

    elif difficulty_choice == "3":
        selected_difficulty = "Hard"
        break

    print("❌ Invalid choice.")


# ----------------------------------------
# Load Questions
# ----------------------------------------

questions = QUESTIONS[selected_category][selected_difficulty]

# Shuffle questions every game
random.shuffle(questions)

score = 0
lives = 3
total_questions = len(questions)

print("\n" + "=" * 55)
print(f"Category   : {selected_category}")
print(f"Difficulty : {selected_difficulty}")
print(f"Lives      : ❤️❤️❤️")
print("=" * 55)
print("\nThe quiz is starting...\n")

# ----------------------------------------
# Quiz Loop
# ----------------------------------------

for question_number, question in enumerate(questions, start=1):

    print("=" * 55)
    print(f"Question {question_number} of {total_questions}")
    print(f"Score : {score}")
    print(f"Lives : {'❤️' * lives}")
    print("=" * 55)

    print("\n" + question["question"])

    answer = input("Your Answer: ").strip().lower()

    if answer == question["answer"]:

        score += 1

        print("\n✅ Correct!")

    else:

        lives -= 1

        print("\n❌ Incorrect!")
        print(f"Correct Answer: {question['answer'].title()}")

        if lives > 0:
            print(f"\n❤️ Lives Remaining: {'❤️' * lives}")

    print(f"\nCurrent Score: {score}/{question_number}")

    input("\nPress Enter to continue...")

    print("\n" * 2)

    # ----------------------------
    # Game Over
    # ----------------------------

    if lives == 0:

        print("=" * 55)
        print("💀 GAME OVER!")
        print("=" * 55)

        print(f"\nYou finished with a score of {score}/{total_questions}")

        percentage = (score / total_questions) * 100

        print(f"Percentage: {percentage:.1f}%")

        save_history(
            selected_category,
            selected_difficulty,
            score,
            total_questions
        )

        best = get_personal_best()

        if score > best:

            print("\n🏆 Congratulations!")
            print("You achieved a NEW Personal Best!")

            save_personal_best(score)

        else:

            print(f"\n🏆 Personal Best: {best}")

        break

else:

    # ----------------------------
    # Player finished every question
    # ----------------------------

    print("=" * 55)
    print("🎉 QUIZ COMPLETE!")
    print("=" * 55)

    percentage = (score / total_questions) * 100

    print(f"\nFinal Score : {score}/{total_questions}")
    print(f"Percentage  : {percentage:.1f}%")

    # ----------------------------
    # Grade
    # ----------------------------

    if percentage == 100:
        grade = "A+"
        message = "Outstanding!"

    elif percentage >= 80:
        grade = "A"
        message = "Excellent!"

    elif percentage >= 70:
        grade = "B"
        message = "Very Good!"

    elif percentage >= 60:
        grade = "C"
        message = "Good!"

    elif percentage >= 50:
        grade = "D"
        message = "Pass"

    else:
        grade = "F"
        message = "Keep Practicing!"

    print(f"Grade       : {grade}")
    print(message)

    # ----------------------------
    # Save Quiz History
    # ----------------------------

    save_history(
        selected_category,
        selected_difficulty,
        score,
        total_questions
    )

    # ----------------------------
    # Personal Best
    # ----------------------------

    best = get_personal_best()

    if score > best:

        save_personal_best(score)

        print("\n🏆 NEW PERSONAL BEST!")

        print(f"Old Best : {best}")
        print(f"New Best : {score}")

    else:

        print(f"\n🏆 Personal Best: {best}")

# ----------------------------------------
# Main Menu
# ----------------------------------------

# ----------------------------------------
# Play Again
# ----------------------------------------

while True:

    again = input("\nWould you like to play again? (Yes/No): ").strip().lower()

    if again == "yes":

        print("\nRestarting the quiz...\n")

        # Restart the program
        import os
        import sys

        os.execv(sys.executable, ["python"] + sys.argv)

    elif again == "no":

        print("\n🏆 Personal Best:", get_personal_best())
        print("👋 Thanks for playing Quiz School!")
        break

    else:

        print("❌ Please enter Yes or No.")
