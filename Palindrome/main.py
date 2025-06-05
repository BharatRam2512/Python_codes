def is_palindrome(str):
    if str == str[::-1]:
        return "Palindrome"
    return "Not a Palindrome"
str=input("Enter a string: ")
print(is_palindrome(str))