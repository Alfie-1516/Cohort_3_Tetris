"""The Grid class manages a 20x10 grid for a Tetris game, handling grid initialization, checking cell status,
clearing and moving rows, resetting the grid, and drawing the grid on a Pygame screen.
"""
import pygame
from Colors_Class import Colors


class Grid:
    def __init__(self):
        # Initialize grid dimensions and cell size
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        # Create a 2D grid array initialized with zeros
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]

        # Get colors for cells from Colors class
        self.colors = Colors.get_cell_colors()

    # Print the current state of the grid to the console (for debugging)
    def print_grid(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end=" ")
            print()


    def is_inside(self, row, column):
        if row >= 0 and row < self.num_rows and column >= 0 and column < self.num_cols:
            return True
        return False

    # Check if the specified cell is empty
    def is_empty(self, row, column):
        if self.grid[row][column] == 0:
            return True
        return False

    # Check if the specified row is fully occupied
    def is_row_full(self, row):
        for column in range(self.num_cols):
            if self.grid[row][column] == 0:
                return False
        return True

    # Clear all cells in the specified row
    def clear_row(self, row):
        for column in range(self.num_cols):
            self.grid[row][column] = 0

    # Move the specified row down by a given number of rows
    def move_row_down(self, row, num_rows):
        for column in range(self.num_cols):
            self.grid[row + num_rows][column] = self.grid[row][column]
            self.grid[row][column] = 0

    # Clear all full rows in the grid and move rows above them down
    def clear_full_rows(self):
        completed = 0
        for row in range(self.num_rows - 1, 0, -1):
            if self.is_row_full(row):
                self.clear_row(row)
                completed += 1
            elif completed > 0:
                self.move_row_down(row, completed)
        return completed

    # Reset the grid to its initial empty state
    def reset(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                self.grid[row][column] = 0


    # Draw the grid on the screen
    def draw(self, screen):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]
                # Define rectangle for each cell to draw
                cell_rect = pygame.Rect(column * self.cell_size + 11, row * self.cell_size + 11,
                                        self.cell_size - 1, self.cell_size - 1)
                # Draw the cell with corresponding color
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)