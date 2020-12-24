def missingElement(Arr1, Arr2):

    count = {}

    for i in Arr1:
        if i not in count:
            count[i] = 1

        else:
            count[i] += 1

    for i in Arr2:
        if i not in count:
            count[i] = 1
        else:
            count[i] +=1
    
    for i in count:
        if count[i] == 1:
           return i


def missingelement(Arr1, Arr2):
    Arr1.sort()
    Arr2.sort()

    for k, j in zip(Arr1, Arr2):
      if k != j:
          return k


if __name__ == "__main__":
    print(missingelement([1,2,3,4,5,6,7,8],[3,7,2,1,4,6,5]))