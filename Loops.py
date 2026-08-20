n=int(input())
count=1
while count<=n:
    if count%3==0 and count%5==0:
        print(count)
    count=count+1