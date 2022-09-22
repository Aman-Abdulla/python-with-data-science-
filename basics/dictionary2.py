from pprint import pp

movies = {}

movies['top gun maverick'] = 8.3
movies['sunday']= 4.2


pp(movies)

for i in movies:
    print(i)

print('only value')
for i in movies:
    print(movies[i])

print('using dict.items() method')
for k,v in movies.items():
    print(k,v)

#user input

for i in range(3):
    name = input('movie name :')
    rating = float(input('movie rating :'))
    movies[name] = rating

print('using dict.items() method')
for k,v in movies.items():
    print(k,v)