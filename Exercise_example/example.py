shop_name = input("enter your shop name:")
TAX_RATE = 1.1
DISCOUNT = 10.0

item_price = float(input("enter ur price:"))
item_iq = int(input("enter number of item:"))
member = input("are u a member:") == "yes"

total = item_price * TAX_RATE * item_iq

if member.strip().lower() == "yes":
    total = total - (total * DISCOUNT / 100) 
else:
    total = total
print(shop_name)
print(total)