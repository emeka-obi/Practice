#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'mystery' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY letter as parameter.
#

def countMovesToBecomePalindrome(word): 
    rightIndex = len(word) // 2  + (len(word) % 2)
    leftIndex = (rightIndex - 1) if len(word) % 2 == 0 else rightIndex - 2
    total_moves = 0 
    
    while (leftIndex >= 0 and rightIndex < len(word)): 
        total_moves += abs(ord(word[leftIndex]) - ord(word[rightIndex]))
        leftIndex -= 1
        rightIndex += 1 
    return total_moves

def mystery(letter):
    # Write your code here
    result = [countMovesToBecomePalindrome(word) for word in letter]
    return result 


if __name__ == '__main__':
    print(mystery('123'))