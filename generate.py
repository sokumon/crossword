import pandas as pd
import numpy as np
import random

ori = ['down','across']
max_row_size = 13
max_col_size = 13
data = pd.read_csv("useful.csv")
grid = np.zeros((max_row_size, max_col_size)) 
# grid[max_row_size][max_col_size] 
# print(len(grid))
def choose_word():
    song_id = data['id'][random.randrange(0,data.shape[0])]
    row_data = data.iloc[song_id]
    return row_data

def choose_first_pos():
    word_ori = random.choice(ori)
    first_word = choose_word()
    x_pos = random.randrange(0,grid.shape[0]-len(first_word))
    y_pos = random.randrange(0,grid.shape[0]-len(first_word))
    

def place_on_grid(word,xpos,ypos,ori):
    if ori == "down":
        for i in range(0,len(word)):
            grid[xpos][ypos+i] = word[i]
    else:
        for i in range(0,len(word)):
            grid[xpos+i][ypos] = word[i]