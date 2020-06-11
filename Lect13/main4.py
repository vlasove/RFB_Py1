# А. Кулинар
m = int(input())
soups = []

for _ in range(m):
    soups.append(input())

n_days = int(input())
for _ in range(n_days):
    n_soups = int(input())
    for _ in range(n_soups):
        current_soup = input()
        if current_soup in soups:
            idx = soups.index(current_soup)
            del soups[idx]
            
soups.sort()

for s in soups:
    print(s)

