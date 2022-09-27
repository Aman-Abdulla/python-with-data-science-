def get_salary():
    val = int(input("enter amt"))
    fine = .09
    sal = val* fine
    return sal

print(get_salary())
ans = get_salary()
print ("salary",ans)


def amount():
     P = int(input("enter value"))
     r = float(input("enter rate"))
     t = int(input("enter amount"))
     si = P+ r + t / 100
     amt = si + p
     return amt, si
amt,si = amount()
print()





def word_count(msg):
    words = msg.split()
    return len(words)

word_count("this is time to go")



