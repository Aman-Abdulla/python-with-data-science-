def mean(*numbers):
    if not numbers:
        return None
    return sum(numbers)/len(numbers)
mean(1,2,3,40)
print(mean(1,2,1,1,2,3,1,321,13,123,312))
print(mean())

