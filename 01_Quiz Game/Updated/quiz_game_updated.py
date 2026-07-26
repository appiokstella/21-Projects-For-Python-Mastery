import os
import sys
import random
from datetime import datetime
from questions import QUESTIONS

PERSONAL_BEST_FILE = "personal_best.txt"
HISTORY_FILE = "quiz_history.txt"
MAX_LIVES = 3


if not os.path.exists(PERSONAL_BEST_FILE):
    with open(PERSONAL_BEST_FILE, "w") as file:
        file.write("0")

if not os.path.exists(HISTORY_FILE):
    open(HISTORY_FILE, "w").close()


def get_personal_best():
    """Return the saved personal best score."""

    try:
        with open(PERSONAL_BEST_FILE, "r") as file:
            return int(file.read())

    except (FileNotFoundError, ValueError):
        return 0


def save_personal_best(score):
    """Save a new personal best score."""

    with open(PERSONAL_BEST_FILE, "w") as file:
        file.write(str(score))


def save_history(player, category, difficulty, score, total):
    """Save each quiz attempt."""

    now = datetime.now()

    percentage = (score / total * 100) if total else 0

    with open(HISTORY_FILE, "a") as file:

        file.write(
            f"{player} | "
            f"{now.strftime('%d/%m/%Y')} | "
            f"{now.strftime('%H:%M:%S')} | "
            f"{category} | "
            f"{difficulty} | "
            f"{score}/{total} | "
            f"{percentage:.1f}%\n"
        )


print("=" * 60)
print("Welcome to Quiz Game!")
print("=" * 60)

player_name = input("\nEnter your name: ").strip().title()

play = input("\nDo you want to play? (Yes/No): ").strip().lower()

if play != "yes":
    print("\n Thanks for visiting Quiz Game!")
    quit()


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

    print(" Invalid choice. Please try again.")

selected_category = categories[choice - 1]


print("\nChoose Difficulty\n")

print("1. Easy")
print("2. Medium")
print("3. Hard")

while True:

    difficulty = input("\nEnter your choice: ")

    if difficulty == "1":
        selected_difficulty = "Easy"
        break

    elif difficulty == "2":
        selected_difficulty = "Medium"
        break

    elif difficulty == "3":
        selected_difficulty = "Hard"
        break

    print("Invalid choice.")


questions = QUESTIONS[selected_category][selected_difficulty]

random.shuffle(questions)

score = 0
lives = MAX_LIVES
total_questions = len(questions)

print("\n" + "=" * 60)
print(" Game Settings")
print("=" * 60)

print(f"Player      : {player_name}")
print(f"Category    : {selected_category}")
print(f"Difficulty  : {selected_difficulty}")
print(f"Lives       : {'❤️' * lives}")
print(f"Questions   : {total_questions}")

print("=" * 60)

input("\nPress Enter to begin the quiz...")
print()

for question_number, question in enumerate(questions, start=1):

    print("=" * 60)
    print(f"Question {question_number} of {total_questions}")
    print(f"Score : {score}")
    print(f"Lives : {'❤️' * lives}")
    print("=" * 60)

    print("\n" + question["question"])

    answer = input("\nYour Answer: ").strip().lower()

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

    if lives == 0:

        print("\n" + "=" * 60)
        print("GAME OVER!")
        print("=" * 60)

        break

    input("\nPress Enter for the next question...")
    print("\n")


percentage = (score / total_questions * 100) if total_questions else 0

print("\n" + "=" * 60)
print("QUIZ RESULTS")
print("=" * 60)

print(f"Player      : {player_name}")
print(f"Category    : {selected_category}")
print(f"Difficulty  : {selected_difficulty}")
print(f"Score       : {score}/{total_questions}")
print(f"Percentage  : {percentage:.1f}%")


if percentage == 100:
    grade = "🏆 A+"
    message = "Outstanding! Perfect Score!"

elif percentage >= 80:
    grade = "🥇 A"
    message = "Excellent Work!"

elif percentage >= 70:
    grade = "🥈 B"
    message = "Very Good!"

elif percentage >= 60:
    grade = "🥉 C"
    message = "Good Job!"

elif percentage >= 50:
    grade = "D"
    message = "You Passed!"

else:
    grade = "F"
    message = "Keep Practicing!"

print(f"Grade       : {grade}")
print(message)

save_history(
    player_name,
    selected_category,
    selected_difficulty,
    score,
    total_questions
)

best = get_personal_best()

if score > best:

    save_personal_best(score)

    print("\n NEW PERSONAL BEST!")
    print(f"Previous Best : {best}")
    print(f"New Best      : {score}")

else:

    print(f"\n Personal Best : {best}")


print("\n" + "=" * 60)
print(" Your quiz attempt has been saved.")
print(" Thanks for playing Quiz School!")

again = input("\nWould you like to play again? (Yes/No): ").strip().lower()

if again == "yes":

    print("\nRestarting Quiz School...\n")

    os.execv(sys.executable, [sys.executable] + sys.argv)

else:

    print("\n Goodbye, see you next time!")
    print("=" * 60)
