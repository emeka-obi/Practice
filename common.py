
example = "emeka believes strongly in christianity and suppport christian virtues"

def count(example):
    dict = {}
    for i in example:
        if i in dict:
            dict[i] +=1
        else:
            dict[i] = 1

    max = 0
    for j in dict:
        if dict[j] > max:
            max = dict[j]
    return max, j





print(count(example))