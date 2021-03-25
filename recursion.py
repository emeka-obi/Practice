
def rec_sum(n):
    if n == 0:
        return 0
    else:
        return n + rec_sum(n-1)

def sum_func(n):
    if n == 0: 
        return 0
    else:
        digits = n % 10
        n = n//10
        return digits + sum_func(n)

def word_split(S,arr, output = None):
    if output is None:
        output = []

    for i in arr:
        if S.startswith(i):
            output.append(i) 
            return  word_split(S[len(i): ],arr, output)

    return output
      
def reverse_string(string, output = None):
    if output is None:
        output = []

    for letter in string:
        last = len(string) - letter - 1
        output.append(last)
    
        



if __name__ == "__main__":
    print(sum_func(34215))
    print(word_split('themanran', ['the','man','ran']))