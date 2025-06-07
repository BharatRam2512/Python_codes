def reverse(x):
    if x>=0:
        r= int(str(x)[::-1])
    elif x<0:
        r1= --int(str(-x)[::-1])
        r=-1*r1
    if -2**31 <= r <= 2**31-1:
        return r
    return 0
x=int(input("Enter a number: "))
print(reverse(x))
