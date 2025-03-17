import cv2
import numpy as np

def read_puzzle():

    # Load image
    image_path = "screenshot.png"  # Change to your image file
    image = cv2.imread(image_path)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert to RGB for display

    # Convert to grayscale and threshold to detect the grid
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)  # Invert to detect grid

    # Find contours and get the bounding box of the grid
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    x, y, w, h = cv2.boundingRect(contours[0])  # Get bounding box

    # Crop the image to remove white space
    cropped_image = image[y:y+h, x:x+w]

    # Get new dimensions
    grid_size = 8  # Assuming 8×8 grid
    cell_w = w // grid_size
    cell_h = h // grid_size

    # Create a NumPy array to store color numbers
    grid = np.zeros((grid_size, grid_size), dtype=int)

    # Determine the color of each cell in the grid
    colors = []
    for row in range(grid_size):
        for col in range(grid_size):

            # Sample a pixel from a little way into the cell (but not the very centre in case a pre-populated queen is there)
            cell_x_sample_point = int((row+0.2) * cell_w)
            cell_y_sample_point = int((col+0.2) * cell_h)
            sample_pixel = cropped_image[cell_x_sample_point, cell_y_sample_point]

            # add to the list of colors if not seen before
            if not any(np.array_equal(sample_pixel, color) for color in colors):
                colors.append(sample_pixel)

            # Get the index of the sample_pixel in colors and add to grid
            color_index = next(i for i, color in enumerate(colors) if np.array_equal(sample_pixel, color))
            grid[row][col]=color_index
    
    return (grid)


def display_grid(grid):
    for row in grid:
        print(" ".join(map(str, row)))

def display_solved_message(execution_time):
    print (f"\nExecution time: {execution_time} seconds")
    message = f"Queens #320 | {round(execution_time,2)}s\n"+ "First 👑s: 🟦 🟩 ⬜\n" + "lnkd.in/queens."
    print (f"\n{message}\n\n")


if __name__ == "__main__":

    grid = read_puzzle()
    display_grid(grid)
