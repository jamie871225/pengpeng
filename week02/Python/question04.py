def twoSum(nums, target):
    x=[]
    for a,b in enumerate(nums):
        if target-nums[a] in nums:
            x.append(a)
    return x
result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9
