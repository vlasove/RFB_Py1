message = input().lower()
correct_words = set(["да", "ад"])

if len(message) != 0 and (message[0] + message[-1]) in correct_words:
    print("СОГЛАСЕН")
else:
    print("НЕ СОГЛАСЕН")