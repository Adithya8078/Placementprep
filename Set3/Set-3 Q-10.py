n=int(input())
z=n
average=0;sum=0
while(n!=0):
    l=float(input())
    sum+=l
    n=n-1
average=sum/z
print(f"The average is: {average:.3f}")