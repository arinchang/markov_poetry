# import nltk
from nltk.tokenize import word_tokenize

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
