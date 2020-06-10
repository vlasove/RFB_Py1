message = "Hello my name is Bob"
words_list = message.split()
print(words_list)

answer = "\n".join(words_list)
print(answer)

nums = [1,2,3,4]
print(" ".join([str(x) for x in nums]))