import pandas as pd
import numpy as np
import random
from word import Word, words_in_grid


ori = ['down','across']
max_row_size = 13
max_col_size = 13
only_words_on_grid = []
already_placed_words = []
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


potenial_next_words = []
choosen_intersection = []
for ts in range(0,3):
    intersection = intersections[words_in_grid[ts].word]
    if ts == 0:
        # first word is placed anywhere

        print("Potenaial next words for "+words_in_grid[ts].word+" are")
        while (len(potenial_next_words) == 0):
            for j in range(0,len(intersection)):
                if intersection[j] != False and len(intersection[j]) == 1:
                    print(words_in_grid[ts].word,intersection[j],words_in_grid[j].word)
                    potenial_next_words.append(words_in_grid[j]) 
                    choosen_intersection.append(intersection[j])
        
            if len(potenial_next_words) == 0:
                words_in_grid[ts].choosen_word()
            else:
                place_anywhere(words_in_grid[ts])
                print("First word is placed at x ",words_in_grid[ts].x,"y",words_in_grid[ts].y)
                already_placed_words.append(words_in_grid[ts].word)
        
    else:
        prev_word = words_in_grid[ts-1]
        print("No of options for "+prev_word.word+"are"+str(len(potenial_next_words)))
    
        # print(choosen_intersection)
        print("Choosing "+str(ts) +" word")
        next_word = Word()
        
        # oritention for new word fixed
        next_word.orientation = 'down'
        if prev_word.orientation == 'down':
            next_word.orientation = 'across'

        while (len(potenial_next_words) > 0):
            rand_num = random.randrange(0,len(potenial_next_words))
            random_potenial_next_word = potenial_next_words[rand_num]
            temp_char = choosen_intersection[rand_num]
            print(prev_word.word)
            print(random_potenial_next_word.word)
            if random_potenial_next_word.word in already_placed_words:
                print("hello")
                potenial_next_words.remove(random_potenial_next_word)
                choosen_intersection.remove(temp_char)
                continue
            else:
                if next_word.orientation == 'down':
                    if len(random_potenial_next_word.word) + prev_word.y < max_col_size :
                        next_word.word = random_potenial_next_word.word
                        next_word.id = random_potenial_next_word.id
                        next_word.x = prev_word.x - random_potenial_next_word.word.index(temp_char)
                        next_word.y = prev_word.y + prev_word.word.find(temp_char)
                        print("Next word x  is",next_word.x)    
                        print("Next word y is ",next_word.y)
                        
                        next_word.place_on_grid(grid)
                        already_placed_words.append(next_word.word)

                        potenial_next_words.remove(potenial_next_words[rand_num])
                        choosen_intersection.remove(choosen_intersection[rand_num])
                        break
                    else:
                        potenial_next_words.remove(potenial_next_words[rand_num])
                        choosen_intersection.remove(choosen_intersection[rand_num])
                else :
                    if len(random_potenial_next_word.word) + prev_word.x < max_row_size:
                        next_word.word = random_potenial_next_word.word
                        next_word.id = random_potenial_next_word.id
                        next_word.x = (prev_word.x + prev_word.word.index(temp_char))
                        next_word.y = (prev_word.y - random_potenial_next_word.word.index(temp_char))
                        print("Next word is " + next_word.word)
                        print("Next word x  is ",next_word.x)    
                        print("Next word y is ",next_word.y)
                

                        next_word.place_on_grid(grid)
                        already_placed_words.append(next_word.word)

                        potenial_next_words.remove(potenial_next_words[rand_num])
                        choosen_intersection.remove(choosen_intersection[rand_num])


                        break
                    else:
                        potenial_next_words.remove(potenial_next_words[rand_num])
                        choosen_intersection.remove(choosen_intersection[rand_num])


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