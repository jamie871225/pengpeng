def maxZeros(nums):
    x=[]
    sum=1
    a=0
    b=len(nums)
    for i in nums:
        if i==0:
            if i==nums[a+1]:
                sum+=1
                x.append(sum)
            else:
                sum=1
        a+=1
        if a==b-1:
            break
    if x!=[]:
        print(max(x))
    else:
        print(0)
maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1]) # 得到 0