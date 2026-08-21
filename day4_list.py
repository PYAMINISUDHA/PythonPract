# Given a list of numbers, find the largest and smallest element without using max() or min().
li=[4,6,2,7,9,11,54,23,44]
large=li[0]
small=li[0]
 
for i in li:
     if i>large:
        large=i
     if i<small:
        small=i
print("largest element in the list : "+str(large))
print("smallest element in the list : "+str(small))

# given a list, create a new list containing only the even numbers.
new_li=[]
for i in li:
    if i%2==0:
        new_li.append(i)
print("the new list containg even numbers : "+str(new_li))

# Given [10, 20, 10, 30, 20, 40, 30], remove the duplicates and create a list containing only unique values.
list1= [10, 20, 10, 30, 20, 40, 30]
new_list=[]
for i in list1:
    if i in new_list:
        pass
    else:
        new_list.append(i)
print("after removing duplicates from  list : "+str(new_list))

# Given a list of numbers, find the second-largest element.
for i in li:
    secound_large=0
    if i<large and i>secound_large:
        secound_large=i
print("from li the secound large element :"+ str(secound_large))
     
        













