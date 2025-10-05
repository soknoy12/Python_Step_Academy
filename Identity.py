x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z) #return true because z is the same subject as x
print(x is y) #return false becasue x is not the same object as y, event if they have the same content 
print(x == y) #to demonstrate the difeerence between "is" and "==": this comparation returns true because ....

#print(x is not z)
#print(x is not y)
#print(x != y)
print("banana" in x) #True
print("pineapple" not in x) 
