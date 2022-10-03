nums = [1,2,3,4,5,6,7,8,9,5,8,5,2,1,6,4,5,8,5,6,5,4,4,5,4]
names = ['ajay singh','vijay pratap','gunja thakur']

num_sqr = list(map(lambda i:i ** 2,nums))
print(num_sqr)


num_eql1 = list(map(lambda i: i+4 * i**2,nums))
print(num_eql1)

short_names =tuple(map(lambda nm: nm.split()[0], names))
print(short_names)
