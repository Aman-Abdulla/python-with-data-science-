x=[1,2,3,0,5,0,8,0,9]

for i in x:
    if i== 0:
        continue
    print(i)


i = 1
while i <= 5:
    data = input('enter data')
    if len(data) ==0:
        continue
    print(f'you entered a value of size {len(data)}')
    i +=1