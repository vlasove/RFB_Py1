words = set()

n = int(input())
for i in range(n):
    word = input()
    words.add(word)


new_word = input()

if new_word in words:
    print("НЕ ЗАСЧИТАНО")
else:
    print("ЗАСЧИТАНО")