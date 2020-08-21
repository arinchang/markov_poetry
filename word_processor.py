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
for token in aggregate:
    if token not in word_list:
        word_list.append(token)

for word in word_list:
    temp_dict = {}
    for i in range(len(aggregate) - 1):
        if aggregate[i] == word:
            if aggregate[i + 1] not in temp_dict:
                temp_dict[aggregate[i + 1]] = 1
            else:
                temp_dict[aggregate[i + 1]] += 1
    corpus[word] = temp_dict

def generate_poem():
    first_word = random.choice(list(corpus.items()))[0]
    poem = first_word
    curr = first_word
    while len(poem) < 1000:
        next_word = choose_next(curr)
        poem += next_word
        curr = next_word

        # max_val = 0
        # max_key = ''
        # for key, val in corpus[curr].items():
        #     if val > max_val:
        #         max_val = val
        #         max_key = key
        # poem += max_key
        # curr = max_key

    return poem


# chooses next word of the poem
def choose_next(curr):
    """
    have a dictionary of words and frequencies with which they appear after each word in corpus

    planning:
    -need to select one to be next word, where the probability that one of the words is selected is proportional to its frequency
    -proability is frequency/total frequencies in the list of values
    -could either make a list that contains each word as many times as its frequency and randomly select
    -or use numpy...?

    todo:
    -assign probability to each word in corpus[curr]

    """

    probability_list = []
    for key, val in corpus[curr].items():
        for i in range(val):
            probability_list.append(key)
    word = random.choice(probability_list)
    return word
