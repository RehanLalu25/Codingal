row_Size = int(input("Enter the number of rows"))
if row_Size%2== 0:
    half_diamond_row = int(row_Size/2)
else:
    half_diamond_row = int(row_Size/2)+1
space = half_diamond_row-1
# upper part
for i in range(1,half_diamond_row + 1):
    for j in range(1,space + 1):
        print(end = " ")
    space = space - 1
    num = 1
    for j in range(2*i-1):
        print(end = str(num))
        num = num + 1
    print()
space = 1
# lower part 
for i in range(1,half_diamond_row):
    for j in range(space):
        print(" ",end = "")
    space = space + 1
    num = 1
    for j in range(1,2*(half_diamond_row-i)+1):
        print(num,end= "")
        num = num + 1
    print()     