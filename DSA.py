#R-1.1
def is_multiple(n, m):
    for i in range(100):
        if n == m * i:
            return True
    else:
        return False
# print(is_multiple(3, 5))


#R-1.2
def is_even(k):
    return k % 2 == 0

# print(is_even(8))

#R -1.3
def minmax(*data):
    largest = data[0]
    smallest = data[0]
    
    for i in data:
        if i > largest:
            largest = i
    
    for k in data:
        if k < smallest:
            smallest = k
       
    return largest, smallest

# print(minmax(3,9,5,6,8,9,10,12))

#R-1.4
def sumsquares(n):
    sum = 0
    for i in range(n):
        sum += i*i
    return sum
    
# print(sumsquares(6))


def easier(n):
  return  sum(i*i for i in range(n))

# print(easier(6))

def sumpsquares(n):
    sum = 0
    for i in range(n):
        if i % 2 !=0:
            sum += i*i
    return sum
# print(sumpsquares(6))

def peasier(n):
    return  sum(i*i for i in range(n) if i % 2 != 0)

print(peasier(6))

#R-1.10
for i in range(8, -9, -2):
     print(i)

# print([i for i in range(1,257) if 256 % i == 0 ])

import random

#Creativity
def reverse(x):
    reverse = []
    for i in range(len(x)):
        bottom = (len(x) -1) - i
        digits = x[bottom]
        reverse.append(digits)
    return reverse

print(reverse([3,2,1]))
x = [1,2,3]
print(sorted(x, reverse=True))
    
def distinct(x):
    dict1 = {}
    for i in x:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
    for k in dict1:
        if dict1[k] > 1:
            return False
        else:
            return  True

print(distinct([1,2,3,4,5]))
    # second way is to compare to a set
    # return set(x) == x

def alpha():
    import string
    return  list(string)


def dotp(a,b):
    c =list()
    for i in range(len(a)):
        output = a[i] * b[i]
        c.append(output)
    return c
print(dotp([1,3,5], [6,7,8]))

def noofvowels(S):
    count = 0
    for i in S:
        if i in ['a', 'e', 'i', 'o', 'u']:
            count += 1
    return count
        

print(noofvowels("emeka is a good boy"))
  

def copy(Sentence):
    str = " "
    import string
    x = [i for i in Sentence if i in list(string.ascii_lowercase)]
    return str.join(x)



print(copy('emeka, is such a bad ass: why? '))

def stringBits(str):
    return str[::2]

print(stringBits('HEllo'))

def doubleChar(s1):
    char_list  = list()
    for i in s1:
        new_char = i * 2
        char_list.append(new_char)
    new_str = ''
    return new_str.join(char_list)
print(doubleChar("Hello"))


def count_evens(nums):
    count = 0
    for i in nums:
        if i % 2 == 0:
            count += 1
    return count

print(count_evens([2,1,2,3,4]))


def arrayCheck(nums):
   
    for i in range(len(nums) -2):
        if nums[i] == 1 and nums[i+1] == 2 and nums[i + 2] == 3:
            return True
    return False

print(arrayCheck([1,1,2,4,1]))