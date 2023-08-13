import pandas as pd
import numpy as np
import random
from word import Word, words_in_grid


ori = ['down','across']
max_row_size = 13
max_col_size = 13
# grid is the board on which the words are placed
grid = np.zeros((max_row_size, max_col_size)) 
# print(grid)

def place_anywhere(wordObject):
    word_ori = random.choice(ori)
    wordObject.choose_orientation(word_ori)
    x_pos = random.randrange(0,max_row_size- len(wordObject.word))
    wordObject.xpos(x_pos)
    y_pos = random.randrange(0,max_col_size- len(wordObject.word))
    wordObject.ypos(y_pos)
    wordObject.place_on_grid(grid)


first_word = Word()
first_word.choose_word()
print("first word is "+ first_word.word)
place_anywhere(first_word)
words_in_grid.append(first_word.word)

# print(words_in_grid)


print(len(words_in_grid))

while(len(words_in_grid) < 13):
    new_word = Word()
    new_word.choose_word()
    print("new word is "+ new_word.word)
    words_in_grid.append(new_word.word)

# print(grid)