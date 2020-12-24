def sentence_reversal(S):
    my_list = []
    for i in range(len(S)):
        str = ""
        reverser = len(S) - i -1 
        my_list.append(S[reverser])
    return str.join(my_list)

        


print(sentence_reversal("Emeka is a boy"))