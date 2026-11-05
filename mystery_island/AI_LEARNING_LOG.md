# AI Learning Log
## Project: Mystery Island – The Lost Lighthouse

### Entry 1: Debugging and Problem Solving

**Task:** Fixing the Lighthouse inventory requirement.

**Problem encountered:**
My game continued displaying "You need a Lantern to enter the Lighthouse!" even when the Lantern was already in my inventory.

**How I used AI:**
I shared my `can_enter_location()` function and the relevant section of my `main.py` file with AI. I asked it to help identify the problem.

**What AI helped me discover:**
AI identified an indentation and conditional-structure problem. The Lighthouse condition was outside the correct conditional block.

**What I learned:**
I learned that indentation in Python determines how conditional statements are grouped. I also learned to inspect the code around an error instead of changing random lines.

**How I verified the solution:**
I corrected the indentation, ran the game again, collected the Rope and Lantern, and successfully reached the Lighthouse.

### Entry 2: Modular Programming and Automated Testing

**Task:** Separating game logic and writing automated tests.

**Problem encountered:**
My game logic was inside `main.py`, making individual parts harder to test independently.

**How I used AI:**
I asked AI to explain modular programming and demonstrate how to separate reusable functions from the main game.

**What AI helped me discover:**
I learned how to create `game_logic.py`, move the route and inventory-checking functions into it, and import them into `main.py`.

I also learned how to use Python's `unittest` module to test individual functions.

**What I learned:**
I learned that functions make programs easier to organise, reuse, maintain, and test. I also learned the difference between a passing test and a failing test.

**How I verified the solution:**
I ran:

```bash
python3 -m unittest discover -s test -v
```

All eight automated tests passed.

---

## Reflection: What I Learned From Using AI

Using AI during this project helped me understand how to approach programming problems instead of simply looking for ready-made solutions. I learned how to identify bugs, understand Python indentation, organise code into separate modules, and write automated tests. I also discovered that AI can make mistakes or misunderstand code, so I must always review suggestions and verify them by running my program. This experience taught me that AI is a learning and problem-solving assistant, but I am responsible for understanding, testing, and improving the code I build.