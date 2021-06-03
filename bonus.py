#Program Name: bonus.py
#Assignment Module 4
#Class 44680 Block 44599 Section 01
#Michael Baumli
#Date: 20210602
#Taken from the example:

#Bonus 
#Sorced from http://textfiles.com/programming/diagnose.txt
diagnose = open("diagnose.txt")
diagnosetext = diagnose.read()
word = ""
word_counts = {}
#print(diagnosetext)
#print(diagnose.read())
for word in diagnosetext.split():
    if word in word_counts:
        word_counts[word] +=1 
    else: 
        word_counts[word] = 1

print(f'{"WORD":<12}COUNT')
for word, count in sorted(word_counts.items()):
    print(f'{word:<12}{count}')

print('\nNumber of unique words:', len(word_counts))

diagnose.close()