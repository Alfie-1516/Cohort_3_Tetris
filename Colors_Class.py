"""The Colors class defines a set of RGB color constants and provides a class method get_cell_colors that returns a
list of specific cell colors."""


# A function to create the different colors of the blocks in the grid
class Colors:
    dark_gray = (26, 31, 40)  # This color represents the empty cell
    green = (47, 230, 23)
    red = (232, 18, 18)
    orange = (226, 116, 17)
    yellow = (237, 234, 4)
    purple = (166, 0, 247)
    cyan = (21, 204, 209)
    blue = (13, 64, 216)
    white = (255, 255, 255)
    dark_blue = (44, 44, 127)
    light_blue = (59, 85, 162)

    @classmethod
    def get_cell_colors(cls):
        return [cls.dark_gray, cls.green, cls.red, cls.orange, cls.yellow, cls.purple, cls.cyan, cls.blue]