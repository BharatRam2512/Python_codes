def longestPalindrome(s):
    s1=""
    for i in range(len(s)):
        for j in range(i,len(s)):
            ss=s[i:j+1]
            if ss==ss[::-1]:
                if len(ss)>len(s1):
                    s1=ss
    return s1
s=input("Enter a string: ")
print("Longest palindromic substrings:", longestPalindrome(s))