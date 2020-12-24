def twoSum(self, nums, target):
    lst = []
    bal = 0
    for i in range(len(nums)):
        bal = target - nums[i]
        for j in range(len(nums)):
            if nums[j] == bal:
                if j == i:
                    continue
                else:
                
                    lst.append(i)
                    lst.append(j)
            
    return set(lst)
            