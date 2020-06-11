a_list = [1,2,3]
b_list = a_list[:] # a_list.copy()

nums = [str(x ** 2) for x in range(0, 11)]
print(nums)


letters = ["a", "b", "c", "d"]
answer = " * ".join(letters)
print(answer)

new_nums = [1,2,3,4]
print(", ".join([str(x) for x in new_nums]))