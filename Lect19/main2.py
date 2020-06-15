fhand = open("input.txt", "r")
string_list = fhand.readlines()
for line in string_list:
    print(line.strip())
fhand.close()