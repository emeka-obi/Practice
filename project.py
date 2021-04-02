def random_number():
    import random
    numbers = [1,2,3,4,5,6,7,8,9]
    compare_list = []
    for i in range(3):
       random_generator = random.choice(numbers)
       compare_list.append(random_generator)
    return compare_list

def Message():
    print("Welcome code breaker! Let's see if you can guess my 3 digit number! \n Code has been generated, please guess a 3 digit number")

def guess():
    compare_list = []
    user_guess = list(int(input("What is your guess: ")))
    for i in user_guess:
        x = int(i)
        compare_list.append(x)
    
    return compare_list
        

def clues(x, y):
    if x == y:
         return "Match"
    elif x[0] == y[0] and x[1] == y[1] or x[1] == y[1] and x[2] == y[2] or x[0] == y[0] and x[2] == y[2]:
        return "Close"
    else:
        return "Nope"

def main():
    Message()
    while True:
        y = random_number()
        x = guess()
        z = clues(x,y)
        if z == 'Match':
            print("Match")
            break
        elif z == 'Close':
            print("Close")
            continue
        else:
            print("Nope")
            continue
        
         
       


if __name__ == "__main__":
    main()



    
