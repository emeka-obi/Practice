# Without using recursion


def string_reverse(s):

    for i in range(len(s)//2):
        last = len(s) - i - 1
        s[last], s[i] = s[i], s[last]

    return s

# using recursion


def string_reversal(s):
    def helper(left, right):
        if left <= right:
            s[left], s[right] = s[right], s[left]
            helper(left + 1, right - 1)

    helper(0, len(s) -1)

    return s

if __name__ == "__main__":
    print(string_reverse(["P","e","t","e","r"]))
    print(string_reversal(["P","e","t","e","r","i","s","i","b","o","r"]))

