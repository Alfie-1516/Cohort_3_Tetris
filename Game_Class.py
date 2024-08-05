"""The Game class manages the Tetris game's state, including the grid, blocks, current and next blocks, score,
sounds, and gameplay mechanics such as block movement, rotation, and collision detection."""

from Grid_Class import Grid
from Diff_Blocks import *
import random
import pygame
class Game:
    def __init__(self):
        # Initialize the game grid and blocks
        self.grid = Grid()
        self.blocks = [IBlock(), JBlock(),LBlock(),  OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()

    # Get a random block from the list of blocks
    def get_random_block(self):
        if len(self.blocks) == 0:
            self.blocks = [IBlock(), JBlock(),LBlock(),  OBlock(), SBlock(), TBlock(), ZBlock()]
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block

    # Move the current block left by one column
    def move_left(self):
        self.current_block.move(0, -1)
        # Check if the block is still inside the grid; if not, move it back
        if not self.block_inside():
            self.current_block.move(0, 1)

    # Move the current block right by one column
    def move_right(self):
        self.current_block.move(0, 1)
        print(self.current_block)
        # Check if the block is still inside the grid; if not, move it back
        if not self.block_inside():
            self.current_block.move(0, -1)

    # Move the current block down by one row
    def move_down(self):
        self.current_block.move(1, 0)
        # Check if the block is still inside the grid; if not, move it back
        if not self.block_inside():
            self.current_block.move(-1, 0)

    # Rotate the current block
    def rotate(self):
        self.current_block.rotate()
        # Check if the block is still inside the grid after rotation; if not, undo the rotation
        if not self.block_inside():
            self.current_block.undo_rotation()

    # Check if the current block is inside the grid boundaries
    def block_inside(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_inside(tile.row, tile.column) == False:
                return False
        return True

    # Draw the game grid and the current block on the screen
    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen)