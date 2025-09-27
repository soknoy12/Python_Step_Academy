#comparison operator
 
# > greater than , < less than , == equal to ,
# >= greater than or equal to , <= less than or equal to
#it only reture true or false
#example

# x = 5
# y = 3

# print(x > y)


#logical operator

# there are three clause in logical operator 
#(and), (or), (not)
#(and) reture true if both statements are true, if one is true the return is false
#example of (and)

# x = 5
# y = 2

# print(x > 2 and x < 6)

#(or) reture true if one of the two statement is true

#example

# print(x > 2 or x < 3)

#(not) reverse the reture of the statement if x is true then (not) reverse to false

#example

# print(not(x < 2))

#Exercise

# age = int(input("How old are you?: "))

# if age >= 13 and age >= 19:
#     print("You are a teenager")
# else: print("You are not a teenager")


# Identity operators

# x = ["Apple", "Banna"]
# y = ["Apple", "Banana"]
# z = x
# print(x is z)
# print(x is y)
# print(x == y)

# print(x is not z)
# print(x is not y)
# print(x != y)

# Membership operators 
#to check if the object is inside the list or array 
#example
# x = ["apple", "banana"]

#Logical choice constructions (IF, ELSEIF, ELSE) or Condition 
#SYNTAX
# if condition:
    #block of code if
# code after if

#example

age = int(input("Enter your age: "))

#alogorith

#2 - 13 is child
#13 - 18 is teenager
#18- 25 is adult
#25- 30 is mature

if age >= 2 and age < 13:
    print("You are a child")
elif age >= 13 and age < 18:
    print("You are a teenager")
elif age >= 18 and age < 25:
    print("You are a adult")
elif age >= 25 and age < 30:
    print("You are a mature")
else:
    print("Invalid")