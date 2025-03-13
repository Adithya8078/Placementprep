row,column=map(int,input().strip().split())
matrix1=[]
matrix2=[]
sum1=[[0 for _ in range(column)] for _ in range(row)]
for i in range(row):
    matrix1.append(list(map(int, input().split())))
for i in range(row):
    matrix2.append(list(map(int, input().split())))   
for i in range(row):
    for j in range(column):
        sum1[i][j]=matrix1[i][j]+matrix2[i][j]
print("First Matrix:")
for row in matrix1:
    print(" ".join(map(str, row)))
print("Second Matrix:")
for row in matrix2:
    print(" ".join(map(str, row)))  
print("Sum of the two matrices is:")
for row in sum1:
    print(" ".join(map(str, row)))