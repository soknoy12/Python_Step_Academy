#Shopping bill calculator program-Part-1
# Shop_name = "Walmart"
# Tax = 0.10  #10% formular total amount = Item_price + sale_tax, sale_tax = Item_price * Tax
# Item_price = 100.5
# Item_quantity = 4
# Member = True

# sale_tax = Item_price * Tax
# total_amount = (Item_price + sale_tax) * Item_quantity

# print("Shop name", Shop_name)
# print(f"Your sale tax per item is: {sale_tax}")
# print(f"Your total amount is {total_amount}")


#shopping input
# shope_name = input("Enter your shop name:")
# Item_quantity = int(input("Enter your item:"))
# Item_price = float(input("Enter your price:"))
# is_member = input("Are you a member?") 

# TAX_RATE = 1.1
# DISCOUNT = 10.0 #Discount 10%

# total = Item_price * TAX_RATE * Item_quantity

# if is_member.strip().lower() == "yes":
#     total = total - (total * DISCOUNT / 100)
# elif is_member:
#     total = total

# print(total)


#shopping cart and discount

#INPUT AND OUTPUT
# shop = input("Enter your shop: ")
# Item_price = float(input("Enter your Item price: "))
# Item_quantity = int(input("Enter your Item quantity: "))
# member_check = input("Are you a memeber: ")

# #TAX
# TAX_RATE = 1.1
# #DISCOUNT 10% = 00.1
# DISCOUNT = 0.1

# #PROCESS 

# total = Item_price * TAX_RATE * Item_quantity

# #CONDITION 


# if member_check.strip().lower() == "yes":
#     total = total - (total * DISCOUNT / 100)
#     print(f"Your shop name is: {shop}")
#     print(f"Your total price with 10% discount is: {total}")
# elif member_check.strip().lower():
#     total = total
#     print(f"Your shop name is: {shop}")
#     print(f"Your total price is: {total}")



#Exercise

age = int(input("How old are you?: "))


if age >= 13 and age <= 19:
    print("You are a teenager")
else:
    print("You are not a teenager")