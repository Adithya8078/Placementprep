n=int(input());f=0
l=list(map(int, input().split()))
target=int(input())
for i in range(0,n-1):
    for j in range(i+1,n):
        if (l[i]+l[j]==target):
            f=1
if f==1:
    print("Yes")
else:
    print("No")
    