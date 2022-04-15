def stringComprehension(S):
    count = {}
    for i in S:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1
    my_list = []
    for j in count:
        my_list.append(j)
        my_list.append(str(count[j]))
    return " ".join(my_list)


print(stringComprehension("AAAAAaaaBBBBCCCDDEEE"))

        

