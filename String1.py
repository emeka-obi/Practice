def twoStrings(s1, s2):
    count = {}
    for i in s1:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1
    check = count.copy()
    
    for i in s2:
        if i in count:
            count[i] -= 1
    
    for j in count:
        if count[j] != check[j]:
            pass

    print(count.items(), check.items())
    
 

if __name__ == "__main__":
    print(twoStrings('aardvark','apple'))