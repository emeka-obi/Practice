def isSubstring(s1, s2):
    if s2.count(s1) > 0:
        return True
    else:
        return False


def Hackerrank_in_a_string(s):
    str1 = "hackerrank"
    my_list = []
    my_list.extend(str1)
 
    for i in s:
        if i == my_list[0]:
            my_list.pop(0)
            if len(my_list) == 0:
                return True
    return False



print(Hackerrank_in_a_string("hereiamstackerrank"))