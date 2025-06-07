def palindromic_substring(str):
    str1=" "
    for i in range(len(str)):
        for j in range(i, len(str)):
            ss=str[i:j+1]
            if ss==ss[::-1]:
                str1+=ss
        return len(set(str1))
str=input("Enter a string: ")
print("Number of unique palindromic substrings:", palindromic_substring(str))
