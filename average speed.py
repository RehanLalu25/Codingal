s1 = int(input("Enter your first speed "))
s2 = int(input("Enter your second speed "))
s3 = int(input("Enter your third speed "))
avg = (s1 + s2 +s3)/3
print(avg)
if s1 < avg:
    print("speed 1 is slower than the average in the difference of ",avg - s1)
if s2 < avg:
    print("speed 2 is slower than the average in the difference of ",avg - s2)
if s3 < avg:
    print("speed 3 is slower than the average in the difference of ",avg - s3)        
    