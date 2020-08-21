# import nltk
from nltk.tokenize import word_tokenize
import random

f_arise = open('arise.txt')
f_change1 = open('changing_places1.txt')
f_change2 = open('changing_places2.txt')
f_change3 = open('changing_places3.txt')
f_persimmons = open('persimmons.txt')
f_gift = open('gift.txt')
f_nocturne = open('nocturne.txt')
f_eating = open('eating_together.txt')
f_bossoms = open('bossoms.txt')

split_aggregate = f_arise.read().split()
split_aggregate += f_change1.read().split()
split_aggregate += f_change2.read().split()
split_aggregate += f_change3.read().split()
split_aggregate += f_persimmons.read().split()
split_aggregate += f_gift.read().split()
split_aggregate += f_nocturne.read().split()
split_aggregate += f_eating.read().split()
split_aggregate += f_bossoms.read().split()

aggregate = word_tokenize(f_arise.read())
aggregate += word_tokenize(f_change1.read())
aggregate += word_tokenize(f_change2.read())
aggregate += word_tokenize(f_change3.read())
aggregate += word_tokenize(f_persimmons.read())
aggregate += word_tokenize(f_gift.read())
aggregate += word_tokenize(f_nocturne.read())
aggregate += word_tokenize(f_eating.read())
aggregate += word_tokenize(f_bossoms.read())

corpus = {}
word_list = []
for token in split_aggregate:
    if token not in word_list:
        word_list.append(token)

for word in word_list:
    temp_dict = {}
    for i in range(len(split_aggregate) - 1):
        if split_aggregate[i] == word:
            if split_aggregate[i + 1] not in temp_dict:
                temp_dict[split_aggregate[i + 1]] = 1
            else:
                temp_dict[split_aggregate[i + 1]] += 1
    corpus[word] = temp_dict

def generate_poem():
    first_word = random.choice(list(corpus.items()))[0]
    poem = first_word
    curr = first_word
    while len(poem) < 1000:
        next_word = choose_next(curr)
        poem += ' ' + next_word
        curr = next_word
    return poem


# chooses next word of the poem
def choose_next(curr):
    probability_list = []
    for key, val in corpus[curr].items():
        for i in range(val):
            probability_list.append(key)
    word = random.choice(probability_list)
    return word
