from helper import read
data = read('pride_n_prejudice.txt')
print(len(data))
newData = data[3:53]
print(newData)

'''
formatting functions
-lower
-upper
-swapcase
-capitalize
-title
-casefold

-ljust
-rjust
-casefold
-centre
'''

print(newData.lower())
print(newData.upper())
print(newData.swapcase())
print(newData.capitalize())
print(newData.title())



word = 'hello'
spacing = 20

ljust = word.ljust(spacing,'*')
print(ljust)

rjust = word.rjust(spacing,'-')
print(rjust)

cen = word.center(spacing,'%')
print(cen)

print(newData.isupper())
print(newData.islower())
print(newData.isalpha())
print(newData.isnumeric())


# utility functions

idx = newData.find("pride")
print(f'pride was found at index {idx}')

idx2 = data.index("in")
print(f'in was found at index {idx2}')
