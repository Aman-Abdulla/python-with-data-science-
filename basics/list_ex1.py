movies = ['sholay','baghban','ddlj','ironman','rrr','inception','kung fu panda','suryavansham','batman']

print(len(movies))

print(movies)

movies.sort()
print(movies)

print('first movie',movies[0])
print('last movie',movies[-1])
print('first 3 movies',movies[:3])
print('all movies except first 3',movies[4:])
print('movies with even indexes',movies[::2])
