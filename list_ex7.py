fib = [0,1]

for i in range(15):
    fib.append( fib[-1] + fib[-2])
    print(fib)
    