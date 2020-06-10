n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

a = int(input()) #1 | 0
b = int(input()) #3 | 2

print(sum(nums[a - 1: b]))