n1 = list(input().strip())  
n2 = list(input().strip())

if sorted(n1) != sorted(n2):  
    print("false")
else:
    print("true")
