import pandas as pd
import numpy as np
import random

ori = ['down','across']
max_row_size = 13
max_col_size = 13

data = pd.read_csv("useful.csv")
lyric_indexes = pd.read_csv("useful_indexes.csv")
lyrics = pd.read_csv("useful_lyrics.csv")

class Word():

    def __init__(self):
        self.id = 0
        self.word = ""
        self.orientation = ""
        # self.x = 0
        # self.y = 0
        self.lyrics = ""
        

    def choose_index(self):
        song_id = data['id'][random.randrange(0,data.shape[0])]
        row_data = data.iloc[song_id]
        return row_data

    def choose_orientation(self,word_ori):
        self.orientation = word_ori

    def pick_word(self):
        choosen_index = self.choose_index()
        choosen_word = ""
        if choosen_index['track_word_count'] > 1:
            choosen_word = choosen_index['track_intials'].strip()
        else:
            choosen_word = choosen_index['track_titles'].strip()
 
        self.word = choosen_word
        self.id = choosen_index['id']
        end_random = lyric_indexes[lyric_indexes['id'] == 0]['size'][0]
        rand_num = random.randrange(0,end_random)
        self.lyrics = lyrics.iloc[rand_num]['lyric']
        

