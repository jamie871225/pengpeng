def maxProduct(nums):
    # 請用你的程式補完這個函式的區塊
    a=sorted(nums, reverse=True)
    b=sorted(nums)
    x=a[0]*a[1]
    y=b[0]*b[1]
    if x>y:
        print(x)
    else:
        print(y)
maxProduct([5, 20, 2, 6]) # 得到 120 因為 20 和 6 相乘得到最大值
maxProduct([10, -20, 0, 3]) # 得到 30 因為 10 和 3 相乘得到最大值