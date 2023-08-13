import pandas as pd
import numpy as np
import random

ori = ['down','across']
max_row_size = 13
max_col_size = 13
words_in_grid = []
data = pd.read_csv("useful.csv")

class Word():

    def __init__(self):
        self.id = 0
        self.word = ""
        self.orientation = ""
        self.x = 0
        self.y = 0
        

    def choose_index(self):
        song_id = data['id'][random.randrange(0,data.shape[0])]
        row_data = data.iloc[song_id]
        return row_data

    def choose_orientation(self):
        word_ori = random.choice(ori)
        self.orientation = word_ori

    def choose_word(self):
        choosen_index = self.choose_index()
        choosen_word = ""
        if choosen_index['track_word_count'] > 1:
            choosen_word = choosen_index['track_intials']
            self.word = choosen_word
            self.id = choosen_index['id']
        else:
            choosen_word = choosen_index['track_titles']
            self.word = choosen_word
            self.id = choosen_index['id']


    def xpos(self):
        x_pos = random.randrange(0,max_row_size- len(self.word))
        self.x = x_pos


    def ypos(self):
        y_pos = random.randrange(0,max_col_size- len(self.word))
        self.y = y_pos


    def place_on_grid(self,grid):
        print(self.word)
        if self.orientation == "down":
            for i in range(0,len(self.word)):
                # grid[self.x][self.y+i] = self.word[i]
                if grid[self.x][self.y+i] == 0:
                    grid[self.x][self.y+i] = ord(self.word[i])
        else:
            for i in range(0,len(self.word)):
                # grid[self.x+i][self.y] = self.word[i]
                if grid[self.x+1][self.y] == 0:
                    grid[self.x+i][self.y] = ord(self.word[i])