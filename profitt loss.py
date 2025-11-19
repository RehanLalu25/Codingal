cp = float(input("Enter cost Price:"))
sp = float(input("Enter selling price:"))
if sp > cp:
    profit = sp-cp
    print("Profit:", profit)
else:
    loss = cp-sp
    print("loss:", loss)
