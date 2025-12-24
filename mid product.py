num = int(input("enter the number!!!!!!!!"))
t = num
numlen = 0
while t > 0:
    numlen = numlen + 1
    t = int(t/10)
if numlen >= 4:
    numlen = int(numlen/2)
    chk = 0
    while num > 0 :
        REM = num%10
        if chk == numlen:
            mid1 = REM
        elif chk ==(numlen - 1):
            mid2 = REM
            num = int(num/10)
            chk = chk +1  
        prod = mid1*mid2
        print("product of mid digit are ",prod)
    else:
        print("its not a four or four digit number")    
            
           