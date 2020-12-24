def canPlaceFlowers(flowerbed,  n):
        count = 0
        for i in flowerbed:
            if i == 0:
                count +=1 


        sum1= 3
        for i in range(2,n+1):
            sum1 += 2 
        print(sum1)
            
        if count < sum1:
            return False
        else:
            return True
            


print(canPlaceFlowers([1,0,0,0,0,0,0,0,1], 3))