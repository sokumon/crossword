import pandas as pd
import numpy as np
import random
from word import Word,words_in_grid


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
place_anywhere(first_word)
print("first word is "+ first_word.word)
# print(words_in_grid)


second_word = Word()
second_word.choose_word()
print("second word is "+ second_word.word)
# for existing_word in words_in_grid:
#     intersection = ''.join(set(second_word.word).intersection(existing_word)) 
#     print(intersection)
#     if intersection != '':
#         print("intersection found")
#         if first_word.orientation == "down":
#             second_word.orientation = "across"
#             second_word.x 
#         else:
#             second_word.orientation = "down"
#             second_word.x = first_word.x + first_word.word.index(intersection)
#             print(second_word.x)
#     else:
#         print("intersection not found")
#         place_anywhere(second_word)


print(grid)