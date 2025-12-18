num = int(input("ENTER THE THREE DIGIT NUMBER "))
SUM = 0
TEMP = num
while TEMP > 0:
    digit = TEMP % 10
    SUM += digit**3
    TEMP//= 10
if num == SUM:
    print(num,"IS AN ARMSTORNG NUMBER!!")
else:
    print(num,"IS NOT AN ARMSTRONG NUMBER!!!!!")        