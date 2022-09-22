ans = 0

while true:
    num = input('enter a number')
    if num.isnumeric():
        ans += int(num)
        else:
            breakprint('total =',ans)
            