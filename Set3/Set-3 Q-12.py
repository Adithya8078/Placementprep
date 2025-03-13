n=int(input())
f=1
if n==0:
    print("0 is not a prime number")
elif n==1:
    print("1 is not a prime number")
else:
    for i in range(2,int(n/2)):
        if n%i==0:
            f=0
            break
if f==1:
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")
            