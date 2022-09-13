msg = " we will be seeing the horizon"


words = msg.split()
print(words)

words = msg.split('e')
print(words)

#replace

update_msg = msg.replace('seeing','viewing')
print(update_msg)

#join()

path = ['user','mypc','documents','data','file.txt']

content = '/'.join(path)

print(content)

#STRIP()

name = "  steve  "
cleaned_name = name.strip()
print(cleaned_name)

from helper import read 
data = read('pride_n_prejudice.txt')

for vowel in 'aeiou':
    print(f'{vowel} => {data.lower().count(vowel)} times')
    
