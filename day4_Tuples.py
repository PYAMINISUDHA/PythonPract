# Given a tuple of numbers, find the sum, maximum, and minimum values.
numbers=(10, 20, 10, 30, 10, 40, 20)
print("Sum:", sum(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))

# Given the tuple (10, 20, 10, 30, 10, 40, 20), find how many times 10 and 20 occur.

numbers = (10, 20, 10, 30, 10, 40, 20)
count10 = 0
count20 = 0

for i in numbers:
    if i == 10:
        count10 += 1
    if i == 20:
        count20 += 1

print("10 occurs:", count10, "times")
print("20 occurs:", count20, "times")

