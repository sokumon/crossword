import pandas as pd
import numpy as np
import random
from word import Word

ori = ['down','across']
words_in_grid = []
max_row_size = 13
max_col_size = 13
only_words_on_grid = []
already_placed_words = []
print("hello")
# grid is the board on which the words are placed
grid = []

def place_on_grid(word,grid):
    print("Word placed to the grid is "+word.word)
    print(word.orientation == "down")
    if word.orientation == "across":
        for i in range(0,len(word.word)):
            if word.y + i < max_col_size:
                if grid[word.x][word.y+i] == 0:
                    grid[word.x][word.y+i] = ord(word.word[i])
            else:
                raise Exception("Word is out of bounds")
    else:
        for i in range(0,len(word.word)):
            if word.x + i < max_row_size:
                if grid[word.x+i][word.y] == 0:
                    grid[word.x+i][word.y] = ord(word.word[i])
            else:
                raise Exception("Word is out of bounds")
            
def print_words ():
    for i in range(0,len(words_in_grid)):
        print(words_in_grid[i].word)


def place_anywhere(wordObject):
    word_ori = random.choice(ori)
    wordObject.choose_orientation(word_ori)
    x_pos = random.randrange(0,max_row_size- len(wordObject.word))
    wordObject.xpos(x_pos)
    y_pos = random.randrange(0,max_col_size- len(wordObject.word))
    wordObject.ypos(y_pos)
    place_on_grid(wordObject,grid)


def generateWords():
    while(len(words_in_grid) < 13):
        new_word = Word()
        new_word.pick_word()
        for i in range(0,len(words_in_grid)):
            if words_in_grid[i].word == new_word.word:
                new_word = Word()
                new_word.pick_word()
 
        words_in_grid.append(new_word)

def regenerateWord(index):
    words_in_grid.pop(index)
    while(len(words_in_grid) < 13):
        new_word = Word()
        new_word.pick_word()
        for i in range(0,len(words_in_grid)):
            if words_in_grid[i].word == new_word.word:
                new_word = Word()
                new_word.pick_word()
 
        words_in_grid.insert(index,new_word)
            
# caluclates all possible intersection for eg one and none one is a three letttered intersections
def calculateIntersections():
    intersections = {}
    for i in range(0,len(words_in_grid)):
        only_words_on_grid.append(words_in_grid[i].word)
        intersections[words_in_grid[i].word] = []
        self_intersection = ''.join(set(words_in_grid[i].word).intersection(words_in_grid[i].word))
        for j in range(0,len(words_in_grid)):
            intersection = ''.join(set(words_in_grid[i].word).intersection(words_in_grid[j].word))
            if len(intersection) == 1 and intersection != self_intersection:
                intersections[words_in_grid[i].word].append(intersection)
            else:
                intersections[words_in_grid[i].word].append(False)
    return intersections
# 
def calculatePotenialWords():
    potenialWords = {}
    for i in range(0,len(words_in_grid)):
            intersection = intersections[words_in_grid[i].word]
            potenialWords[i] = {
                "next_words":[],
                "intersections" :[]
            }
            for j in range(0,len(intersection)):
                if intersection[j] != False and len(intersection[j]) == 1:
                    potenialWords[i]["next_words"].append(words_in_grid[j])
                    potenialWords[i]["intersections"].append(intersection[j])
    
    
    return potenialWords

generateWords()
intersections = calculateIntersections()
# print(intersections)
possible_words =  calculatePotenialWords()
no_of_words = 0
next_few_words = []
prev_word = ""
words_placed_recently = []
while(no_of_words < 13):
    if no_of_words == 0:
        rand_no = random.randrange(0,13)
        print(words_in_grid[rand_no].word)
        print("Pontenial words are ")
        for word in possible_words[rand_no]["next_words"]:
            next_few_words.append(word.word)
        place_anywhere(words_in_grid[rand_no])
        prev_word = words_in_grid[rand_no]
        words_placed_recently.append(prev_word)
        no_of_words = no_of_words + 1
    else:
        print(no_of_words)
        next_word = next_few_words.append(no_of_words)
        no_of_words = no_of_words + 1
        

print(grid)