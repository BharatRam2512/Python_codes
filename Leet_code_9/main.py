def ispalindrome(x):
    if str(x)==str(x)[::-1]:
        return True
    return False

x= int(input("Enter a number: "))
print(ispalindrome(x))