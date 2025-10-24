number_list = [[5, 2, 2], [1, 6, 4], [3, 4, 5], [6, 3, 7]]
all_list = []
for inner in number_list:
    all_list.extend(inner)

unique = []
repeated = []
seen = set()

for item in all_list:
    if item in seen:
        if item not in repeated:
            repeated.append(item)
    else:
        seen.add(item)
        unique.append(item)

print(unique)
print(repeated)