def arrayPairSums(arr1, num):

    if len(arr1) < 2:
        return None

    seen = set()
    output = set()

    for i in arr1:


        target = num - i

        if target not in seen:
            seen.add((i))

        else:
            output.add((min(target, i), (max(target, i))))

    # return '\n'.join(map(str, list(output)))
    return output
    


if __name__ == "__main__":
    print(arrayPairSums([1,3,2,2], 4))
