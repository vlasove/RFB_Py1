age = int(input())
salary = int(input())

if age >= 18 and age <= 25:
    print("Ideal candidate")
    if salary <= 100:
        print("SUPER IDEAL CANDIDATE")

elif age == 29:
    print("U")
else:
    print("Done")