import pandas as pd
import numpy as np
import matplotlib.pyplot as plot
import string
import re


alphabets = []
track_word_count = []
track_intials = []

alphabets = list(string.ascii_lowercase)

data = pd.read_csv("datasets/taylor_swift_lyrics_2006-2022_all.csv")
# print(data.head())

count = np.zeros(26)
track_titles = data['track_title'].unique()
# splits the word and returrns the index for eg all too well becomes atw
def giveInit(song_name):
    intial = ''
    song_names = song_name.split()
    for i in range(len(song_names)):
        intial = intial + song_names[i][0]
    return intial


track_word_len = []
for i in range(len(track_titles)):
    track_titles[i] = track_titles[i].lower()
    temp = track_titles[i].encode('ascii',"ignore")
    track_titles[i] = temp.decode()
    pattern = r'[\[\(].*?[\]\)]'
    clean_text = re.sub(pattern, '', track_titles[i])
    track_titles[i] = clean_text.replace(" ", "")
    track_word_len.append(len(track_titles[i]))
    # anyaled no of songs start with a specific alphabet
    # track_word_count.append(len(track_titles[i].split()))
    # if track_word_count[i] > 1:
    #     track_intials.append(giveInit(track_titles[i]))
    # else:
    #     track_intials.append("NA")
    # for j in range(len(alphabets)):
    #     if track_titles[i].startswith(alphabets[j]):
    #         count[j] = count[j] + 1


print(len(count))
print(len(track_titles))
print(len(track_word_count))
print(len(track_intials))

print(track_titles)

# malplot lib drawing
# plot.bar(alphabets,count,color="red",width=0.9)
# plot.xlabel("alphabets")
# plot.ylabel("count")
# plot.show()

plot.bar(track_titles,track_word_len,color="red",width=0.9)
plot.xlabel("alphabets")
plot.ylabel("count")
plot.show()

for t in range(5):
    print(track_titles[t],track_word_count[t],track_intials[t])

# final_dict = {
#     "track_titles":track_titles,
#     "track_word_count":track_word_count,
#     "track_intials":track_intials
# }
# final_data = pd.DataFrame(final_dict)
# final_data.to_csv("useful.csv")

# data.insert(loc=0, column='id', value=data.track_title.factorize()[0])
# print(data.head())
# data.drop(['track_title'],axis=1,inplace=True)
# data.drop(['album_name'],axis=1,inplace=True)
# data.drop(['track_n'],axis=1,inplace=True)
# data.to_csv("useful_lyrics.csv",index=False)

# data_again = pd.read_csv("useful_lyrics.csv")
# data_new = data_again.groupby(data_again.id,as_index=False).size()
# data_new.to_csv("useful_indexes.csv",index=False)

# random range
# print(random.randrange(0,2))