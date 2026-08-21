def prime(num):
    if num < 2:
        print("it's not a prime")
        return

    count = 0

    for i in range(2, num):
        if num % i == 0:
            count += 1

    if count > 0:
        print("it's not a prime")
    else:
        print("it's a prime number")

prime(2)
# Write a function find_largest(numbers) that takes a list of numbers and returns the largest number without using max().

def find_largest(numbers):
    largest = numbers[0]

    for i in numbers:
        if i > largest:
            largest = i

    return largest


numbers = [4, 6, 2, 7, 9, 11, 54, 23]

result = find_largest(numbers)
print(result)