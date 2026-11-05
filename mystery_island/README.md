# Mystery Island: The Lost Lighthouse

## Project Description

Mystery Island is a beginner-friendly Python text adventure game. The player explores an island, collects useful items, makes decisions, manages energy, and tries to reach the Lost Lighthouse.

## Requirements

- Python 3
- No external libraries required.

## How to Run

1. Clone or download this repository.
2. Open the project folder in your terminal.
3. Run the game:

```bash
python3 main.py
```

## How to Play

- Enter your name to begin.
- Explore to collect useful items.
- Collect the Rope to cross the Old Bridge.
- Collect the Lantern to enter the Lighthouse.
- Make decisions that affect your energy.
- Reach the Lighthouse before your energy runs out.
- Choose whether to play again after finishing.

## Game Locations

1. Beach
2. Jungle
3. Cave
4. Old Bridge
5. Lighthouse

## Game Features

- Player name input.
- Energy management.
- Inventory system.
- Location navigation.
- Item collection.
- Decision-making with consequences.
- Input validation.
- Winning and losing conditions.
- Replay option.

## Running Automated Tests

Run the following command:

```bash
python3 -m unittest discover -s test -v
```

The project currently contains eight automated tests covering routes and inventory requirements.

## Project Structure

```text
mystery_island/
│
├── main.py
├── game_logic.py
├── test/
│   └── test_game.py
└── README.md
```

## Known Limitations

- Location names must be entered with the correct capitalization.
- The game uses a text-based interface.
- The energy and decision system is intentionally simple.

## Learning Objectives

This project helped me practise:

- Python functions.
- Dictionaries and lists.
- Conditional statements.
- Loops.
- Modular programming.
- Automated testing with unittest.
- Debugging and error handling.

## Author

Godwin Ngbede 