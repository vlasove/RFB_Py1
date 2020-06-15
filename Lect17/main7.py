def my_key(elem:int):
    return abs(elem)

nums = [-7,2,3,0,-20, 21, 44] # 0, 2,3,-7,-20, 21,44
nums.sort(key=lambda elem: abs(elem))
print(sorted(nums, key=my_key, reverse=True))
print(nums)