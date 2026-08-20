def number(arr):
    large=arr[0]
    small=arr[0]
    total=0
    for i in arr:
        if i>large:
            large=i
        if i<small:
            small=i
        total=total+i
    print(large)
    print(small)
    print(total)
               
number([12, 5, 8, 21, 4, 15, 10])