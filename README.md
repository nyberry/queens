# Linked in Queens Puzzle Solver

This project is a variation of the N-Queens problem. The goal is to place queens on an 8x8 board following these rules:

- No two queens can be in the same row or column.
- No two queens can be in adjacent squares.
- Each queen must be placed in a distinct coloured region, where regions are represented by numbers in the input grid.
- Unlike the classic N-Queens problem, diagonal constraints do not apply.

## Features
- Reader.py contains functions to loads an initial puzzle grid from a screenshot, saved at screenshot.png
- Queens.py uses a recursive backtracking algorithm to find valid solutions.
- Ensures that each region gets exactly one queen.
- Outputs a composite grid where `👑` marks queen placements and other cells retain their original values.
- Displays execution time for performance analysis.

## Installation
Ensure you have Python installed (3.12 or later). Then, clone this repository:

```sh
git clone https://github.com/nyberry/queens.git
cd queens
```

Install dependencies if needed:
```sh
pip install numpy opencv-python
```

## Usage
Run the solver:

```sh
python queens.py
```

### Example Output
```
Solution:

👑 0 0 0 0 0 1 1
0 0 0 👑 3 1 1 1
0 0 2 2 3 👑 1 1
0 👑 4 4 3 3 3 1
0 5 5 5 6 6 👑 1
0 7 👑 5 6 6 7 1
7 7 7 5 6 7 7 👑
7 7 7 7 👑 7 1 1

Execution time: 0.006999 seconds

Queens #320 | 0.01s
First 👑s: 🟦 🟩 ⬜
lnkd.in/queens.
```

## File Structure
```
queens/
│── queens.py          # Main solver script
│── reader.py          # Loads the puzzle grid
│── README.md          # Project documentation
│── screenshot.png     # Screenshot of the puzzle to solve
```

## Future Improvements
- Could implement a graphical interface for screenshot copy and paste and for solution visualization.
- But I probably won't.

N Berry 2025-Mar-17


