words = ["apple", "banana", "kiwi", "orange", "grape"]
new_li=[]
for i in words:
    if len(i) >5:
        new_li.append(i)
print(new_li)