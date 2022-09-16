books = ['steelheart','firefight','osmosis','calamity']


books.append('the final empire')
books.append('atomic habit')

print(books)



books[5] = "the well of ascension"   #to Update any list



books.insert(3,'legion: skin deep')

print('idx,book')
for i,b in enumerate(books):
    print(f'{i}\t {b}')

fruits = ['apple','banana','cherry','guava']
dry_fruits = ['almonds','cashew']
fruits.extend(dry_fruits)
print(fruits)