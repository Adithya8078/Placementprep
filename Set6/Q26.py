row=int(input())
column=int(input())
n=0
matrix=[]
for i in range(row):
    
    matrix.append(list(map(int,input().split())))
i=0;j=0    
for i in range(row):
    for j in range(column):
        if matrix[i][j]<0:
            n+=1
        else:
            break
print(n)        
    