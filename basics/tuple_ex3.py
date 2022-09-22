#tuple - set - list interchangeable

x = [1,2,34,5,6,7,8,9]
xt = tuple(x) #list to tuple
xl =list(xt) #tuple to list
xs = set(x) # list to set
xl = list(xs) #set to list
xs = set(xt) #tuple to set
xt = tuple(xs) #set to tuple


xyt = ()
xyt = for i in range(5):
    int(input('enter a value=>'))

print(xyt)