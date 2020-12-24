def unique(S):
    count = {}

    for i in S:
        if i not in count:
            count[i] = 1
        else:
            count[i]+= 1
            
    for i in count:
        if count[i] > 1:
            return False
    return True


def unique1(S1):
    char  = set()

    for i in S1:
        if i in char:
            return False
        else:
            char.add(i)

    return True



if __name__ == "__main__":
    print(unique1('abcde'))