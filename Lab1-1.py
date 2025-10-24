numbers = [0,1,3,0,2,0,0,4]
count = 0
for i in range(len(numbers)):
    if numbers[i] != 0:
        numbers[count], numbers[i] = numbers[i], numbers[count]
        count += 1
print(*numbers)
