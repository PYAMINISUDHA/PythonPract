# try:
#     total=int(open("secound.txt").read())
# except FileNotFoundError:
#     print("file is missing")
# except ValueError:
#     print("file is not a number")
# else:
#     print(f"total is{total}")
# finally:
#     print("done checking.")


try:
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))

    bmi = weight / (height ** 2)

except ValueError:
    print("Please enter numbers only.")

except ZeroDivisionError:
    print("Height cannot be zero.")

else:
    print("Your BMI is:", round(bmi, 2))
