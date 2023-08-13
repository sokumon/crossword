import pandas as pd
import numpy as np
import random

ori = ['down','across']
max_row_size = 13
max_col_size = 13
words_in_grid = []
data = pd.read_csv("useful.csv")
grid = np.zeros((max_row_size, max_col_size)) 
# grid[max_row_size][max_col_size] 
print(grid)
class Word():
    def choose_index():
    song_id = data['id'][random.randrange(0,data.shape[0])]
    row_data = data.iloc[song_id]
    return row_data

    def choose_orientation():
        return ori[random.randrange(0,2)]
    





    def place_on_grid(word,xpos,ypos,ori):
        print(word)
        if ori == "down":
            for i in range(0,len(word)):
                if grid[xpos][ypos+i] == 0:
                    grid[xpos][ypos+i] = ord(word[i])
        else:
            for i in range(0,len(word)):
                if grid[xpos+i][ypos] == 0:
                    grid[xpos+i][ypos] = ord(word[i])


choose_first_word()
print(grid)