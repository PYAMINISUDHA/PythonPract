# Given students = {"Rahul": 85, "Priya": 92, "Amit": 78, "Sneha": 95, "Karan": 88}, find the student with the highest marks.
students = {
    "Rahul": 85,
    "Priya": 92,
    "Amit": 78,
    "Sneha": 95,
    "Karan": 88
}

highest =0
student_name =""

for name in students:
    if students[name] > highest:
        highest = students[name]
        student_name = name

print(student_name)
print(highest)

# Given a dictionary containing student names and marks, calculate the average marks.

students = {
    "Rahul": 85,
    "Priya": 92,
    "Amit": 78,
    "Sneha": 95,
    "Karan": 88
}

total = 0

for name in students:
    total = total + students[name]

average = total / len(students)

print("Average marks:", average)

# Take a sentence as input and create a dictionary containing the frequency of each word. Example: "apple banana apple mango banana apple" → {"apple": 3, "banana": 2, "mango": 1}.
sentence = input("Enter a sentence: ")

words = sentence.split()
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print(frequency)

# Given two dictionaries, combine them into a single dictionary.
dict1 = {"a": 10, "b": 20}
dict2 = {"c": 30, "d": 40}

combined = {}

for key in dict1:
    combined[key] = dict1[key]

for key in dict2:
    combined[key] = dict2[key]

print(combined)
