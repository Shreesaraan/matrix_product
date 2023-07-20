def matrix_product(matrix,number):
    result=[[element*number for element in row] for row in matrix]
    return result

matrix=[]
rows=int(input("Enter the Number of Rows : "))
columns=int(input("Enter the Number of Columns : "))
number=int(input("Enter the Number to multiply : "))
print("Enter the Array Elements : ")
for i in range(rows):
    matrix.append(list(map(int,input().split())))
print(matrix_product(matrix,number))