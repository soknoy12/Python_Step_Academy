Shop_name = "Khmer Reader"
Tax = input("Enter tax rate: %")
Item_price = input("Enter item price: ")
Item_quantity = input("Enter item quantity: ")
Membership = input("Enter membership status (yes/no): ")
if Membership.lower() == "yes":
    Membership = "Member"
    discount = 0.1 
if Membership.lower() == "no":
    Membership = "Non-member"
    discount = 0.0
Total_price = float(Item_price) * int(Item_quantity) * (1 + float(Tax) / 100)
Total_price -= Total_price * discount

print("Welcome to " + Shop_name)
print("Tax rate is " + Tax)
print("Item price is " + Item_price)
print("Item quantity is " + Item_quantity)
print("Membership status is " + Membership)
print("Total price is " + str(Total_price))
print("Thank you for shopping with us!")