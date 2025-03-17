import time
import numpy as np
from reader import read_puzzle, display_grid, display_solved_message


# function to check is a cell is a valid place to put a queen
def is_valid(state, row, col, grid, placed_regions_set):
    region = grid[row][col]  # Get the region ID
    
    # Ensure one queen per region
    if region in placed_regions_set:
        return False

    # Ensure no two queens in the same row
    for placed_col in range(col):
        placed_row = state[placed_col]
        if placed_row == row: 
            return False
               
    # Ensure no adjacent queens:
    if col>=1:
        previous_row = state[col-1]
        if abs(previous_row - row) <=1:
            return False
    
    # All checks passed - it's ok to place a queen here
    return True

# recursive function to place queens
def solve(state, col, grid, placed_regions_set, num_queens):
    
    # Base case: all queens placed
    if col == num_queens:
        return [state[:]]

    solutions = []

    for row in range(len(grid)):  # Iterate over all rows
        region_color = grid[row][col]  # Get region color
        if is_valid(state, row, col, grid, placed_regions_set):
            state[col] = row  # Place queen
            new_regions_set = placed_regions_set.copy()  # Copy region set
            new_regions_set.add(region_color)  # Mark region as used
            solutions.extend(solve(state, col + 1, grid, new_regions_set, num_queens))  # Recurse
            state[col] = -1  # Backtrack
    
    return solutions


if __name__ == "__main__":

    initial_grid = read_puzzle()  # Load initial grid
    
    start_time = time.time()

    num_queens = len(np.unique(initial_grid))  # num_queens == rows == cols == color regions
    state = [-1] * num_queens  # Initialize state tracking queen positions. State will be a list of rows, where the index will be cols. -1 means no queen placed.
    solutions = solve(state, 0, initial_grid, set(), num_queens)

    end_time = time.time()

    for solution in solutions:
        num_queens = len(solution)
        queens_grid = np.zeros((num_queens, num_queens), dtype=int)

        # Place queens on the grid
        for col in solution:
            queens_grid[solution[col],col]=1

        # Create composite grid
        composite_grid = np.array(initial_grid, dtype=object)  # Keep numbers but allow "Q"
        for row in range(num_queens):
            for col in range(num_queens):
                if queens_grid[row, col] == 1:
                    composite_grid[row, col] = "Q"  # Place "Q" where a queen is present

    if solutions:
        print("\nSolution:\n")
        display_grid(composite_grid)
        display_solved_message(end_time - start_time)

    else:
        print("No solution found.")
