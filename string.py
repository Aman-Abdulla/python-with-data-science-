
#1


my_string = 'hello people'
print(my_string)


#2

x = input("enter a word=>")
print((len(x)))



#3


y = 'python is great'
slice1 = y[10:15]

print(slice1)



#4

w = 'python is everywhere'
slice2 = w[0:6]
slice3 = w[6:9]
slice4 = w[10:20]

print(slice2)
print(slice3)
print(slice4)


#5

q = 'hello world'
print(q[::-1])

#6

p = 'How are you ?'
print(p.upper())


#7

u = 'How Is It Going ?'
print(u.lower())

#8

words = ['python','is','easy','to','learn']
for item in words:
    print(item,'\n',end="  ")

#11

j = 'the variable is 15'
print(j)

#12

s1 = 'python'
s2 = 'is'
s3 = 'great'

print((s1,s2,s3,)*20)

for i in range (1,10):
    print(f"{i}.")


#13

f = input("enter a sentence :")
print(*f.split(" "), sep='\n')



