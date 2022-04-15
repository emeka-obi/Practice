
def compare_arr(a,b):
    compare_dict = {}
    for i in a:
        if i not in compare_dict:
            compare_dict[i] = 1
        else:
            compare_dict[i] += 1
    
    for k in b:
        if k in compare_dict:
            compare_dict[k] -=1
        else:
            compare_dict[k] = 1
 
 
    for j in compare_dict:
        if compare_dict[j] < 1:
            return False
    return True


if __name__ == "__main__":
    print(compare_arr([5,10,15,20,25,26],[2,4,6,8,10,1]))
    print(compare_arr([5,10,10,15,20,25],[2,4,6,8,12,13]))


# The runtime of this algorith is O(A+B+dict). In the worst case you have to iterate through the contents of both arrays and the dictionary