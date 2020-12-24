def fibonnaci(n):
    a = 0
    b = 1
    if n <= 0:
        print("incorrect input")
    elif n ==1:
        return n

    else:
        for i in range(2,n):
            c = a + b
            a = b
            b = c
            print(c)


print(fibonnaci(9))


def recursive_fibonnaci(n):

    if n <= 0:
        return "Incorrect ouput"
    elif n == 1:
        return 1
    
    elif n == 2:
        return 1

    else:
        return recursive_fibonnaci(n-1) + recursive_fibonnaci(n-2)
