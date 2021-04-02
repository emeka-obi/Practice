def palindrome(s):
    lst = []
    for i in range(len(s)):
        rev = len(s)-i-1
        lst.append(s[rev])
    
    z = "".join(lst)

    return s == z
 
     



print(palindrome('GoG'))
   