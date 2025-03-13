n=int(input());odd=0
for i in range(n):
    l=int(input())
    if l%2!=0:
        odd+=1
if odd==0:
    print("No odd elements are present")
else:
    print("Odd Elements:",odd)