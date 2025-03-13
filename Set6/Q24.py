n=input()
l=list(map(int,n.strip().split(',')))
i=0;j=len(l)-1;diff=0
while(i!=len(l)):
    if((l[j]-l[i])>diff and i!=j):
        diff=l[j]-l[i]
        j=j-1
    if j==i:
        j=len(l)-1
        i=i+1
    else:
        j=j-1

print(diff)