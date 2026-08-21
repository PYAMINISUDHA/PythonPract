# Given two sets, find their union, intersection, and difference.
set_1={3,2,5,6}
set_2={3,5,4,1}

print("union of two sets :"+str(set_1 | set_2))
print("intersection of two sets :"+str(set_1 & set_2))
print("differance between two sets :"+str(set_1-set_2))

# Given a list of numbers, use a set to find all the duplicate elements.
list_l=[3,4,6,7,8,2,3,6,3,6,7]
seen=set()
duplicate=set()

for i in list_l:
    if i in seen:
        duplicate.add(i)
    else:
        seen.add(i)
print("duplicate values :"+str(duplicate))

# Given two sets of student names, find the students who are present in both sets.
set_students1={"yamini","lalitha"}
set_students2={"lalitya","yamini"}
for i in set_students1:
    if i in set_students2:
        print("the common students in both sets :"+i)

    