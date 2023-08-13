import pandas as pd
import numpy as np
import random
from word import Word

max_row_size = 13
max_col_size = 13
# grid is the board on which the words are placed
grid = np.zeros((max_row_size, max_col_size)) 
print(grid)

first_word = Word()
first_word.choose_word()
first_word.choose_orientation()
first_word.xpos()
first_word.ypos()
first_word.place_on_grid(grid)

print(grid)