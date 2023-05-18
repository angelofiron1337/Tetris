import random

# Define the tetrimino_shapes and COLORS lists here
#tetrimino_shapes
tetrimino_shapes = [
    [['.....',
      '.OOO.',
      '.O...',
      '.....'],
     ['.....',
      '..OO.',
      '...O.',
      '...O.',
      '.....'],
     ['.....',
      '...O.',
      '.OOO.',
      '.....'],
     ['.....',
      '.O...',
      '.O...',
      '.OO..',
      '.....']],
     
    [['.....',
      '.OOO.',
      '...O.',
      '.....'],
     ['.....',
      '...O.',
      '...O.',
      '..OO.',
      '.....'],
     ['.....',
      '.O...',
      '.OOO.',
      '.....'],
     ['.....',
      '.OO..',
      '.O...',
      '.O...',
      '.....']],
     
    [['.....',
      '.OOO.',
      '..O..',
      '.....'],
     ['.....',
      '..O..',
      '.OO..',
      '..O..',
      '.....'],
     ['.....',
      '..O..',
      '.OOO.',
      '.....'],
     ['.....',
      '.O...',
      '.OO..',
      '.O...',
      '.....']],
     
    [['.....',
      '.OO..',
      '.OO..',
      '.....']],
     
    [['.....',
      '..OO.',
      '.OO..',
      '.....'],
     ['.....',
      '.O...',
      '.OO..',
      '..O..',
      '.....']],
     
    [['.....',
      '.OO..',
      '..OO.',
      '.....'],
     ['.....',
      '..O..',
      '.OO..',
      '.O...',
      '.....']],

    [['.....',
      '.O...',
      '.O...',
      '.O...',
      '.O...'],
     ['.....',
      '.OOOO',
      '.....']],

]


# COLORS list
COLORS = [
    (0, 255, 255),  # Cyan
    (255, 0, 255),  # Magenta
    (255, 255, 0),  # Yellow
    (0, 255, 0),    # Green
    (0, 0, 255),    # Blue
    (255, 165, 0),  # Orange
    (255, 0, 0),    # Red
]

# Create the Tetrimino class with methods for movement and rotation
class Tetrimino:
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = COLORS[tetrimino_shapes.index(shape)]

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def rotate(self):
        self.shape = rotate(self.shape)

    # Insert the update_shape() method here
    def update_shape(self):
        shape_template = self.shape[random.randint(0, len(self.shape) - 1)]
        self.shape = [list(row) for row in shape_template]

def rotate(shape):
    return [''.join([shape[y][x] for y in range(len(shape))]) for x in range(len(shape[0]))[::-1]]

