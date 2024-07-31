"""This code defines various Tetris block classes (LBlock, JBlock, IBlock, OBlock, SBlock, TBlock, ZBlock),
each inheriting from a base Block class."""

from Position_Class import Position
from Block_Class import Block


class IBlock(Block):
  def __init__(self):
    super().__init__(id = 1)
    self.cells = {
      0: [Position(1, 0), Position(1, 1), Position(1, 2), Position(1, 3)],
      1: [Position(0, 2), Position(1, 2), Position(2, 2), Position(3, 2)],
      2: [Position(2, 0), Position(2, 1), Position(2, 2), Position(2, 3)],
      3: [Position(0, 1), Position(1, 1), Position(2, 1), Position(3, 1)]
    }
class JBlock(Block):
  def __init__(self):
    super().__init__(id = 2)
    self.cells = {
      0: [Position(0, 0), Position(1, 0), Position(1, 1), Position(1, 2)],
      1: [Position(0, 1), Position(0, 2), Position(1, 1), Position(2, 1)],
      2: [Position(2, 0), Position(2, 1), Position(2, 2), Position(2, 2)],
      3: [Position(0, 1), Position(1, 1), Position(2, 0), Position(2, 1)],
    }

class LBlock(Block):
  def __init__(self):
    super().__init__(id = 3)
    self.cells = {
      0: [Position(0, 2), Position(1, 0), Position(1, 1), Position(1, 2)],
      1: [Position(0, 1), Position(1, 1), Position(2, 1), Position(2, 2)],
      2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 0)],
      3: [Position(0, 0), Position(0, 1), Position(1, 1), Position(2, 1)],
    }

class OBlock(Block):
  def __init__(self):
      super().__init__(id = 4)
      self.cells = {
        0: [Position(0, 0), Position(0, 1), Position(1, 0), Position(1, 1)],
        1: [Position(1, 1), Position(0, 0), Position(0, 1), Position(1, 0)],
        2: [Position(0, 0), Position(0, 1), Position(1, 0), Position(0, 1)],
        3: [Position(0, 0), Position(0, 1), Position(1, 0), Position(1, 1)]
      }
class SBlock(Block):
  def __init__(self):
    super().__init__(id = 5)
    self.cells = {
      0: [Position(0, 1), Position(0, 2), Position(1, 0), Position(1, 1)],
      1: [Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 2)],
      2: [Position(1, 1), Position(1, 2), Position(2, 0), Position(2, 1)],
      3: [Position(0, 0), Position(1, 0), Position(1, 1), Position(2, 1)]
    }
class TBlock(Block):
  def __init__(self):
    super().__init__(id = 6)
    self.cells = {
      0: [Position(0, 1), Position(1, 0), Position(1, 1), Position(1, 2)],
      1: [Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 1)],
      2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 1)],
      3: [Position(0, 1), Position(1, 0), Position(1, 1), Position(2, 1)]
    }
class ZBlock(Block):
  def __init__(self):
      super().__init__(id = 7)
      self.cells = {
        0: [Position(0, 0), Position(0, 1), Position(1, 0), Position(1, 1)],
        1: [Position(1, 1), Position(0, 0), Position(0, 1), Position(1, 0)],
        2: [Position(0, 0), Position(0, 1), Position(1, 0), Position(0, 1)],
        3: [Position(0, 0), Position(0, 1), Position(1, 0), Position(1, 1)]
      }