numbers = [10, 25, 30, 45, 50, 75, 90, 100]
new_li=[]
for i in numbers:
    if (i>30 and i%5==0) and i!=75 :
        new_li.append(i)
print(new_li)