info = "Alex was born at 1999\nLive in Moscow\nStud in MSU\n"
info_list =[x + '\n' for x in  ["a", "b", "c"]]

with open("output.txt", "a") as fhand:
    fhand.writelines(info_list)