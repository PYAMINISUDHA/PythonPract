#Take two integers as input and print their sum, difference, product, and division.

first_number=int(input())
secound_number=int(input())
add=first_number+secound_number
sub=first_number-secound_number
mul=first_number*secound_number
div=first_number/secound_number
print(add)
print(sub)
print(mul)
print(div)

# Take a user's name and age as input and print: Hello Rahul, you are 21 years old.
name=input()
age=int(input())
print("hello "+name+" , you are "+str(age)+" years old")

# Take a number as input and check whether it is positive, negative, or zero.

number=int(input())
if number>0:
    print("positive number")
elif number<0:
    print("negative number")
else:
    print("it's zero")

# Take three numbers as input and print the largest number.
a=int(input())
b=int(input())
c=int(input())
if a>=b and a>=c:
    print("a is large")
elif a<=b and b>=c:
    print("b is large")
else:
    print("c is large")
