A guide to using this repo as a learning resource, whether you're following along project-by-project or forking it to run your own version of the challenge.

## Who this is for

- Beginners who know basic Python syntax and want structured, project-based practice instead of another syntax tutorial
- Intermediate learners looking to fill gaps (file I/O, APIs, OOP, algorithms) through small, complete builds rather than isolated exercises
- Anyone who learns better by finishing something real every day than by watching lectures

## Prerequisites

- Python 3.10+ installed
- Comfortable with: variables, basic data types, `if`/`else`, loops
- Not required, but helpful: a GitHub account, if you want to track your own version publicly

## How to use this repo

### Option 1 — Follow along project by project

1. Start at `01_Quiz Game/` and work through the folders in order — difficulty increases roughly in sequence (🟢 Easy → 🟡 Medium → 🔴 Advanced).
2. Read the project's code first without running it. Predict what each function does before checking.
3. Run it, break it on purpose (bad input, edge cases), and see what happens.
4. Rebuild it from scratch in a new file without looking, then compare against the original.
5. Read that project's `README.md` for the concepts it's meant to teach and the honest reflection on what was hard — if you hit the same wall, that's expected, not a sign you're behind.

### Option 2 — Run your own 21-day challenge

1. Fork this repo.
2. Keep the same project list (or swap in ones more relevant to your interests) and the same folder structure — see [Repo Structure](README.md#-repo-structure).
3. Update the **Daily Log** and **Project List** tables in your fork's `README.md` as you go — the visible progress tracker is most of what makes this format work as an accountability tool.
4. Write your own per-project `README.md` for each build: what it does, what you learned, what was hard, what you'd add next. Copying an explanation without writing it yourself skips the part that actually cements the concept.

## What each stage of the project list teaches

| Range | Focus                               | Core skills                                                                                         |
| ----- | ----------------------------------- | --------------------------------------------------------------------------------------------------- |
| 01–06 | Fundamentals through small games    | Functions, loops, conditionals, string/random basics                                                |
| 07–11 | File handling & game logic          | File I/O, encryption basics, structured game state                                                  |
| 12–15 | Graphics, timing, and external data | Turtle graphics, timed loops, JSON, REST APIs                                                       |
| 16–17 | Automation                          | Scripting real tasks (downloading, backups) with standard-library tools                             |
| 18–21 | Algorithms & applied logic          | Game-theory-adjacent logic, event-driven programming (Pygame), classic algorithms (BFS/pathfinding) |

If you're short on time, the 07–11 and 18–21 ranges teach the most transferable skills (file/data handling and algorithmic thinking) — start there if you already have the 01–06 fundamentals down.

## Tips for keeping the daily log honest

- Write the "what was hard" section _before_ the "what I learned" section — it's more honest that way, and it's usually more useful to a future reader (including future-you) than the parts that went smoothly.
- If a project takes more than one day, log it as more than one day. The point of the log is accuracy, not a perfect streak.
- Revisit an early project after finishing a later one — you'll usually spot at least one thing you'd now do differently. That comparison is worth writing down too.

## Contributing your own project variation

If you'd like to suggest an additional project, a fix to an existing one, or an improvement to a `README.md`:

1. Open an issue describing the change first for anything beyond a small fix.
2. Keep the same folder pattern: `NN_Project Name/` containing the code and a `README.md` with the four standard sections (what it does, what I learned, what was hard, what's next).
3. Reference the concepts table above so new projects slot into the existing difficulty progression rather than duplicating an earlier skill.
