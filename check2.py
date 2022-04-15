def isPalindrome(word):
    if len(word) < 2:
        return True
    if word[0] != word[-1]:
        return False
    return isPalindrome(word[1:-1])


# The run time of this algorithm is O(n)


if __name__ == "__main__":
    print(isPalindrome("ana"))
