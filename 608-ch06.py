#Program Name: 608-ch06.py
#Assignment Module 4
#Class 44680 Block 44599 Section 01
#Michael Baumli
#Date: 20210602
#Taken from the example:
# fig06_02.py
"""Tokenizing a string and counting unique words."""

text = ('this is sample text with several words ' 
        'this is more sample text with some different words')

word_counts = {}

# count occurrences of each unique word
for word in text.split():
    if word in word_counts: 
        word_counts[word] += 1  # update existing key-value pair
    else:
        word_counts[word] = 1  # insert new key-value pair

print(f'{"WORD":<12}COUNT')

for word, count in sorted(word_counts.items()):
    print(f'{word:<12}{count}')

print('\nNumber of unique words:', len(word_counts))

#sourced from: http://textfiles.com/programming/ethics.txt

ethics = open("ethics.txt")
ethicstext = ethics.read()
word = ""
word_counts = {}
#print(ethicstext)
#print(ethics.read())
for word in ethicstext.split():
    if word in word_counts:
        word_counts[word] +=1 
    else: 
        word_counts[word] = 1

print(f'{"WORD":<12}COUNT')
for word, count in sorted(word_counts.items()):
    print(f'{word:<12}{count}')

print('\nNumber of unique words:', len(word_counts))

ethics.close()



