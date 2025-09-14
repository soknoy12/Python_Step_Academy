#Identify operator (is ,not is)
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z) #returns True
print(x is y) #returns False
print(x == y) #to demonstrate the difference between " is " "=="

print(x is not z) #False
print(x is not y) #True
print(x != y) #to demonstrate the difference between " is not " "!="

#Membership operator (in, not in)
x = ["apple", "banana"]
print(" banana" in x) #true
print(" apple" not in x) #true
