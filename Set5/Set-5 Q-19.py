n=input()
total=0;available=0
for i in range(len(n)):
    if n[i] == "C":
        if available == 0:
            total += 1
        else:
            available -= 1  
    elif n[i] == "U":
        if available > 0:
            available -= 1  
        else:
            total += 1  
    elif n[i] == "R" or n[i] == "L":
        available += 1  
print(total)        
        