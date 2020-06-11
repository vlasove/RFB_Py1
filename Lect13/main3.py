nums = [10, 20, -10, 30, -4, 50, 6, 100]

new_nums = nums.copy()
new_nums.sort(reverse=True)
print("Original: ", nums)
print("Sort: ", new_nums)


sorted_nums = sorted(nums, reverse=True)
print("Original:", nums)
print("Sorted:", sorted_nums)

print(dir([]))