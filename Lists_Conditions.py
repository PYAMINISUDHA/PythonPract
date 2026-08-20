numbers = [1, 2, 3, 2, 4, 1, 5]

count = 0

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j]:
            count += 1
            break
print(count)