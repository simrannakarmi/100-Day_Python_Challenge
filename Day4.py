# Calculate a bill for a shopping store with discount

customer_name = input("Enter Customer Name: ")
cost = float(input("Enter cost of the product: "))
quantity = float(input("Enter quantity of the product: "))

amount = cost * quantity
gst = amount * 12/100
total_amount = amount + gst

if total_amount < 1000:
    discount = 0
elif total_amount < 3000:
    discount = 0.1 * total_amount
else:
    discount = 0.2 * total_amount

print("-----------------------------")
print(f"Shopping Bill of {customer_name}")
print("-----------------------------")
print(f"Amount: {amount}")
print(f"GST: {gst}")
print(f"Discount: {discount:.2f}")
print(f"Total Amount: {total_amount - discount}")
print("-----------------------------")

