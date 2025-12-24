string = input("Enter your own word")
char = input("Enter your own character")
i = 0
count = 0 
while (i<len(string)):
    if (string[i]==char):
        count = count+1
    i = i+1
print("Total number of times ",char,"has occured= ",count)        
