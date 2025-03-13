n=input()
z=int(input())
l=list(map(int,n.strip().split(',')))
l.sort()
y=len(l)-z
i=0;diff=999999999999999999
while(i<=y):
    v=l[i:i+z]
    maximum=max(v)
    minimum=min(v)
    if maximum-minimum<diff:
        diff=maximum-minimum
        u=v
    i=i+1
print(" ".join(map(str,u)))