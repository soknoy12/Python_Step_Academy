#Input data from Console
#By defaul Input as (string)
#Activity_Practice
#Shop_name 
#TAX_RATE 10% or 0.1
#Item_Price 
#Item_Quantity 
#Are you a member? 

Shop_name = input("Please enter your shop name:")
TAX_RATE = 0.1
DISCOUNT = 10.0 #Discount 10%
Item_Quantity = int(input("Please enter your quantity:"))
Item_Price = float(input("Please enter your Item price:"))
is_Member = input("Are you a member?")

total_price = Item_Price * Item_Quantity * TAX_RATE + Item_Price * Item_Quantity

#is_Member.trip()
#is_Member.lower() == "yes"
#is_Member.upper() == "YES"
#is_Member.capitalize() == "yes"

if is_Member.lower() == "yes":
    total_price = total_price - (total_price * DISCOUNT / 100)
else:
    total_price = total_price

print(Shop_name)
print(total_price)
