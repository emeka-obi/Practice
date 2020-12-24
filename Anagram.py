''''a word, phrase, or name formed by rearranging the letters of another, such as cinema, formed from iceman.'''

def anagram (a, b):

    anagram_dict = {}

    for i in a.lower():
        if i not in anagram_dict:
            anagram_dict[i] = 1
        else:
            anagram_dict[i] += 1
    
    for k in b.lower():
        if k in anagram_dict:
            anagram_dict[k] -=1
        else:
            anagram_dict[k] = 1
 
    print(anagram_dict.items())
    for j in anagram_dict:
        if anagram_dict[j] != 0:
            return False
    return True
    
        



a = "Emeka is b gbat"
b = "Emeka is a goat"

print(anagram(a,b))