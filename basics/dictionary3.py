import helper as h
from string import punctuation
data = h.read('basics/pride_n_prejudice.txt')

print(len(data))

#remove punctuation

for p in punctuation:
    data = data.replace(p,'')

#split into words

words = [word.strip() for word in data.lower().split()]

print('total words words', len(words))
print('unique words found', len(set(words)))


#create a dictionary

wc = {}

for word in set(words):
    wc[word] = words.count(word)

#sorting the dictionary

wc = sorted(wc.items(),key=lambda x: x[1], reverse=True)


#print the top 10 words 

for i in range(10):
    print(wc[i])
