# Quiz Game (Updated Version)

This project is an improved version of the original Quiz Game program. The initial project was a simple five-question computer hardware quiz that asked questions one by one and displayed a final score.

The new version expands on that idea by introducing several new features, making the quiz more interactive, reusable, and enjoyable to play.

## What's New

Compared to the original version, this project now includes:

- Multiple quiz categories (e.g., Python, Science, History)
- Three difficulty levels (Easy, Medium, Hard)
- Three lives before the game ends
- Questions are shuffled every game using `random.shuffle()`
- Personal Best tracking that is saved between sessions
- Quiz history logging with the player's name, category, difficulty, score, percentage, date, and time
- Percentage score calculation
- Grade system (A+ to F) with feedback messages
- Play Again option without manually rerunning the program
- Questions stored separately in `questions.py` for easier maintenance and expansion
- Input validation to reduce invalid user entries
