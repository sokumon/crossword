import pandas as pd
import numpy as np
import random
from word import Word
import json

ori = ['down','across']
grid_dict = {
    "current_word":"",
    "current_word_ori":"",
    "next_word":"",
    "intersection_index_current_word":"",
    "intersection_index_next_word":"",
    "intersection_letter":"",
}

clues_list = []
temp_dict = grid_dict.copy()
# for easy lookup 
titles_only = []
words_in_grid = []
# first word

word = Word()
word.pick_word()
rand_ori = random.choice(ori)
word.choose_orientation(rand_ori)


temp_dict['current_word'] = word.word
temp_dict['current_word_ori'] = word.orientation
clues_list.append(word.lyrics)
titles_only.append(word)

words_in_grid.append(temp_dict)
print(words_in_grid)

# loop for the other words
# choose a word
# check for intersection with previous word with one letter if not choose another
i = 1
prev_intersection = ""
max_iterations = 10 
iterations_with_condition_met = 0
while (i < 13):
    print("i is ",i)
    word_new = Word()
    word_new.pick_word()
    temp = word_new.word
    for z in range(i-1,0):
        word_prev = words_in_grid[i-1]
        print(word_prev)
        intersection = ''.join(set(temp).intersection(word_prev['current_word']))
        print("intersectipon is", prev_intersection)
        if temp != word_prev['current_word']  and len(intersection) == 1 and prev_intersection != intersection:
        # make the dictonaory
        # if i == 1:
        # print("word+prev",word_prev)
            words_in_grid[i-1]['next_word'] = temp
            words_in_grid[i-1]['intersection_letter'] = intersection
            words_in_grid[i-1]['intersection_index_current_word'] = word_prev['current_word'].index(intersection)
            words_in_grid[i-1]['intersection_index_next_word'] = temp.index(intersection)
            # print("grid words",words_in_grid[i-1])
            
            temp_dict_new = grid_dict.copy()
            temp_dict_new['current_word'] = temp

            temp_dict_new['current_word_ori'] = "across"
            
            if word_prev['current_word_ori'] == "across":
                temp_dict_new['current_word_ori'] = "down"
                
            words_in_grid.append(temp_dict_new)
            prev_intersection = intersection
            
            i = i + 1
            iterations_with_condition_met += 1
            if iterations_with_condition_met >= max_iterations:
                break
    




file_name = "data.json"
with open(file_name, 'w') as json_file:
    json.dump(words_in_grid, json_file)



# grid making which will render direcly on the frontend
