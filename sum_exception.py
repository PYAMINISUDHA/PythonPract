try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
 
    sum = num1 + num2
 
    print("Sum =", sum)
 
except ValueError:
    print("Invalid input! Please enter numbers only.")