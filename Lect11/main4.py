last_word = input()

while True:
    current_word = input()
    if last_word[-1] != current_word[0]:
        print(current_word)
        break 
    last_word = current_word
