age = int(input())

if age < 14:
    print("DEMO-VERSION")
    print("WWWW")
    
elif age >= 14 and age < 25:
    print("FULL VERSION")
elif age >= 25 and age < 35:
    print("FULL VERSION + SUBSCRIPTION")
else:
    print("FULL VERSION + FREE GIFT")