"""
URLify: Write a method to replace all spaces in a string with '%20: You may assume that the string 
has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string. 
(Note: If implementing in Java, please use a character array so that you can perform this operation in place.)
"""

def Urlify(S):
    return S.replace(" ", "%20")



def Urlify2(S):
    new_list = list(S)
    for i in range(len(new_list)):
        if new_list[i]  == " ":
            new_list[i] = '%20'

    return "".join(new_list)



if __name__ == "__main__":
    print(Urlify2("Emeka is the best ever"))