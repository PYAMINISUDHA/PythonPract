# Print all numbers from 1 to 100 that are divisible by both 3 and 5.
li=[]
for num in range(1,100):
    if num%3==0 and num%5==0:
        li.append(num)
print("the numbers which are divisible by 3 and 5 :"+str(li))

# Take a number n and print its multiplication table from 1 to 10.
for i in range(1,11):
    for j in range(1,11):
        result=i*j 
        print(f"{i} X {j} = {result}")

# Take a number and find the sum of its digits.
number =input("enter a number to find its sum")
sum=0
for i in number:
    sum=sum+int(i)
print("the sum of digits in number : "+str(sum))

# Take a number and check whether it is a prime number.
Number=int(input("enter a number to check prime or not"))
count=0
for i in range(2,Number//2):
    if Number%i==0:
        count+=1
        
if count>0:
        print(str(Number) + " not a prime")
else:
    print("it's a prime number")
# Print the following pattern for n = 5: *, **, ***, ****, ***** (one row per line).
lines = int(input("give an integer: "))
for i in range(1, lines + 1):
    print(i * "*")