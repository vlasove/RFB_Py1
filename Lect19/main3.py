

with open("input.txt", "r") as fhand:
    window = [5 for x in range(0, 10)]
    for w in window:
        print("New window ", w, "chars")
        string_list = fhand.readlines(w)
        for line in string_list:
            print(line.strip())

#print(fhand.readable())