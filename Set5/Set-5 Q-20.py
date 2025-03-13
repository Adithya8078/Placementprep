n=int(input());flag=0
l = list(map(int, input().split()))  
for i in range(len(l)):
    if l.count(l[i])>1:
        flag=1
        break
if flag==1:
    print("true")
else:
    print("false")
        