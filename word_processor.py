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

split_aggregate = []
split_aggregate.append(f_arise.read().split())
split_aggregate.append(f_change1.read().split())
split_aggregate.append(f_change2.read().split())
split_aggregate.append(f_change3.read().split())
split_aggregate.append(f_persimmons.read().split())
split_aggregate.append(f_nocturne.read().split())
split_aggregate.append(f_eating.read().split())
split_aggregate.append(f_bossoms.read().split())
split_aggregate.append(f_gift.read().split())

corpus = {}
word_list = []

for poem in split_aggregate:
    for token in poem:
        if token not in word_list:
            word_list.append(token)

for word in word_list:
    corpus[word] = {}
    for poem in split_aggregate:
        for i in range(len(poem) - 1):
            if poem[i] == word:
                if poem[i + 1] not in corpus[word]:
                    corpus[word][poem[i + 1]] = 1
                else:
                    corpus[word][poem[i + 1]] += 1

def generate_poem():
    first_word = choose_uppercase()
    poem = first_word
    curr = first_word
    while len(poem) < 400 or curr[-1] != '.':
        next_word = choose_next(curr)
        poem += ' ' + next_word
        curr = next_word
    return poem

#Choose a word that is capitalized
def choose_uppercase():
    uppercase_words = []
    for key, val in corpus.items():
        if key[0].isupper():
            uppercase_words.append(key)
    return random.choice(uppercase_words)

# chooses next word of the poem
def choose_next(curr):
    if curr[-1] == '.':
        return choose_uppercase()
    probability_list = []
    for key, val in corpus[curr].items():
        for i in range(val):
            probability_list.append(key)
    return random.choice(probability_list)

if __name__ == '__main__':
    print(generate_poem())
