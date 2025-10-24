import random

n = int(input())
table = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(random.randint(0, 100))
    table.append(row)

min_val = 101

for i in range(n):
    for j in range(n):
        if table[i][j] < min_val:
            min_val = table[i][j]
positions = []

for i in range(n):
    for j in range(n):
        if table[i][j] == min_val:
            positions.append((i, j))

print("Минимальное значение:", min_val)
print("Позиции:", positions)