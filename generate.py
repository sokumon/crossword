import pandas as pd
import numpy as np
import random
from word import Word, words_in_grid


ori = ['down','across']
max_row_size = 13
max_col_size = 13
only_words_on_grid = []
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




def generateWords():
    while(len(words_in_grid) < 13):
        new_word = Word()
        new_word.choose_word()
        words_in_grid.append(new_word)



def calculateIntersections():
    intersections = {}
    for i in range(0,len(words_in_grid)):
        only_words_on_grid.append(words_in_grid[i].word)
        intersections[words_in_grid[i].word] = []
        self_intersection = ''.join(set(words_in_grid[i].word).intersection(words_in_grid[i].word))
        for j in range(0,len(words_in_grid)):
            intersection = ''.join(set(words_in_grid[i].word).intersection(words_in_grid[j].word))
            if len(intersection) > 0 and intersection != self_intersection:
                intersections[words_in_grid[i].word].append(intersection)
            else:
                intersections[words_in_grid[i].word].append(False)
    return intersections


# print(intersections)"
generateWords()
intersections = calculateIntersections()
# words = ["question","dbatc","apitw","marjorie","happiness","red","sbt","wh","willow","style","sn","sss","ttds"]
# fake_grid = np.zeros((13,13))
# intersections = {'question': [False, 't', 'it', 'ieo', 'nise', 'e', 'ts', False, 'io', 'tse', 'ns', 's', 'ts'], 'dbatc': ['t', False, 'ta', 'a', 'a', 'd', 
# 'tb', False, False, 't', False, False, 'td'], 'apitw': ['it', 'ta', False, 'ia', 'ipa', False, 't', 'w', 'wi', 't', False, False, 't'], 'marjorie': ['ieo', 'a', 'ia', False, 'eia', 're', False, False, 'io', 'e', False, False, False], 'happiness': ['nise', 'a', 'ipa', 'eia', False, 'e', 's', 'h', 'i', 'se', 'ns', 's', 's'], 'red': ['e', 'd', False, 're', 'e', False, False, False, False, 'e', False, False, 'd'], 'sbt': ['ts', 'tb', 't', False, 's', False, False, False, False, 'ts', 's', 's', 'ts'], 'wh': [False, False, 'w', False, 'h', False, False, False, 'w', False, False, False, False], 'willow': ['io', False, 'wi', 'io', 'i', False, False, 'w', False, 'l', False, False, False], 'style': ['tse', 't', 't', 'e', 'se', 'e', 'ts', False, 'l', False, 's', 's', 'ts'], 'sn': [False, False, False, False, False, False, 's', False, False, 's', False, 's', 's'], 'sss': [False, False, False, False, False, False, False, False, False, False, False, False, False], 'ttds': 
# ['ts', 'td', 't', False, 's', 'd', 'ts', False, False, 'ts', 's', 's', False]}
potenial_next_words = []
choosen_intersection = []
for ts in range(0,len(words_in_grid)):
    intersection = intersections[words_in_grid[ts].word]
    if ts == 0:
        # first word is placed anywhere
        place_anywhere(words_in_grid[ts])
        for j in range(0,len(intersection)):
            if intersection[j] != False and len(intersection[j]) == 1:
                print(words_in_grid[ts].word,intersection[j],words_in_grid[j].word)
                potenial_next_words.append(words_in_grid[j]) 
                choosen_intersection.append(intersection[j])
        
    else:
        print(len(potenial_next_words))
        prev_word = words_in_grid[ts-1]
        # print(choosen_intersection)
        print("Choosing "+str(ts) +" word")
        next_word = Word()
        
        # oritention for new word fixed
        next_word.orientation = 'down'
        if prev_word.orientation == 'down':
            next_word.orientation = 'across'

        while (len(potenial_next_words) > 1):
            rand_num = random.randrange(0,len(potenial_next_words))
            random_potenial_next_word = potenial_next_words[rand_num]
            temp_char = choosen_intersection[rand_num]
            print(choosen_intersection)
            print(prev_word.word)
            print(temp_char)
            print(random_potenial_next_word.word)
            if next_word.orientation == 'down':
                if random_potenial_next_word.y + prev_word.y < max_col_size:
                    next_word.word = random_potenial_next_word.word
                    next_word.id = random_potenial_next_word.id
                    next_word.x = prev_word.x - random_potenial_next_word.word.index(temp_char)
                    print(prev_word.word)
                    
                    next_word.y = prev_word.y + prev_word.word.find(temp_char)
                    potenial_next_words.remove(potenial_next_words[rand_num])
                    choosen_intersection.remove(choosen_intersection[rand_num])
                    break
                else:
                    potenial_next_words.remove(potenial_next_words[rand_num])
                    choosen_intersection.remove(choosen_intersection[rand_num])
            else :
                if random_potenial_next_word.x + prev_word.x < max_row_size:
                    next_word.word = random_potenial_next_word.word
                    next_word.id = random_potenial_next_word.id
                    next_word.x = (prev_word.x + prev_word.word.index(temp_char))
                    next_word.y = (prev_word.y - random_potenial_next_word.word.index(temp_char))
                    break
                else:
                    potenial_next_words.pop(potenial_next_words[rand_num])
                    choosen_intersection.pop(choosen_intersection[rand_num])

        print("Next word is " + next_word.word)
        next_word.place_on_grid(grid)
        # while (len(potenial_next_words) > 0 and next_word not in only_words_on_grid):            

            
        #     print("Potential Next word is " + random_potenial_next_word.word)
        #     print(  "choosen intersection is " + temp_char)
        #     # choose orientation based on previous word
        #     random_potenial_next_word.choose_orientation('down')
        #     if words_in_grid[ts-1].orientation == 'down':
        #         random_potenial_next_word.choose_orientation('across')

        #     # choose x and y position based on previous word
        #     # before that check if the word can be placed on the grid like not going out of bounds
        #     # if less than max_row_col size thats great but if not then remove the word from the list and choose another word
        #     if random_potenial_next_word.orientation == "down":
        #         if words_in_grid[ts-1].x + len(random_potenial_next_word.word) < max_col_size:
        #             random_potenial_next_word.xpos(words_in_grid[ts-1].x - random_potenial_next_word.word.index(temp_char))
        #             random_potenial_next_word.ypos(words_in_grid[ts-1].y + words_in_grid[ts-1].word.index(temp_char))
        #             next_word = random_potenial_next_word
        #             print("Final Next Word is"+next_word.word)
        #             break
        #         else:
        #             shift = max_col_size - (words_in_grid[ts-1].x)
        #             words_in_grid[ts-1].xpos(shift)
        #             words_in_grid[ts-1].place_on_grid(grid)
        #             potenial_next_words.remove(random_potenial_next_word)
        #     else:
        #         if words_in_grid[ts-1].y + len(random_potenial_next_word.word) < max_row_size :
        #             random_potenial_next_word.xpos(words_in_grid[ts-1].x +  words_in_grid[ts-1].word.index(temp_char))
        #             random_potenial_next_word.ypos(words_in_grid[ts-1].y +  random_potenial_next_word.word.index(temp_char))

        #             next_word = random_potenial_next_word
        #             print("Final Next Word is"+next_word.word)
        #             break
        #         else:
        #             shift = max_row_size - (words_in_grid[ts-1].y)
        #             words_in_grid[ts-1].ypos(shift)
        #             words_in_grid[ts-1].place_on_grid(grid)
        #             potenial_next_words.remove(random_potenial_next_word)

        # if next_word != "":
        #     print("Placing next word")
        #     next_word.place_on_grid(grid)

        potenial_next_words = []
        choosen_intersection = []
        for j in range(0,len(intersection)):
            if intersection[j] != False and len(intersection[j]) == 1:
                print(words_in_grid[ts].word,intersection[j],words_in_grid[j].word)
                potenial_next_words.append(words_in_grid[j]) 
                choosen_intersection.append(intersection[j])
        
    
        
        # words_in_grid.remove(words_in_grid[ts])
                


            
# for i in range(0,len(words_in_grid)):
#     print(words_in_grid[i].word)
# print(intersections)



# print(grid)