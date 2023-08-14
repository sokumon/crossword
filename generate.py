import pandas as pd
import numpy as np
import random
from word import Word, words_in_grid


ori = ['down','across']
max_row_size = 13
max_col_size = 13
only_words = []
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


# first_word = Word()
# first_word.choose_word()
# print("first word is "+ first_word.word)
# place_anywhere(first_word)
# words_in_grid.append(first_word.word)

# print(words_in_grid)



def generateWords():
    while(len(words_in_grid) < 13):
        new_word = Word()
        new_word.choose_word()
        words_in_grid.append(new_word)

def regenerateWords():
    for word in words_in_grid:
        word.choose_word()

def calculateIntersections():
    intersections = {}
    for i in range(0,len(words_in_grid)):
        only_words.append(words_in_grid[i].word)
        intersections[words_in_grid[i].word] = []
        self_intersection = ''.join(set(words_in_grid[i].word).intersection(words_in_grid[i].word))
        for j in range(0,len(words_in_grid)):
            intersection = ''.join(set(words_in_grid[i].word).intersection(words_in_grid[j].word))
            if len(intersection) > 0 and intersection != self_intersection:
                intersections[words_in_grid[i].word].append(intersection)
            else:
                intersections[words_in_grid[i].word].append(False)
    return intersections


# print(intersections)
generateWords()
intersections = calculateIntersections()

# for i in range(0,3):
#     if i == 0:
#         print(words_in_grid[i].word)
#         print(intersections[words_in_grid[i].word])
#         for j in range(0,len(intersections[words_in_grid[i].word])):
#             if intersections[words_in_grid[i].word][j] != False and :
#                 print(words_in_grid[i].word.index(intersections[words_in_grid[i].word][j]))
for i in range(0,len(words_in_grid)):
    print(words_in_grid[i].word)
print(intersections)



# print(grid)