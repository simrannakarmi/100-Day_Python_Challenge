# Program to calculate Profit and Loss

cp = float(input("Enter the Cost Price: "))
sp = float(input("Enter the Selling Price: "))

if sp > cp:
    print(f"Profit is Rs. {sp-cp}")
elif cp > sp:
    print(f"Loss is Rs. {cp-sp}")
else:
    print("No Profit and No Loss")
    
    