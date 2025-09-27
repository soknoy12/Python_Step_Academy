#Case is use for the alternate of If or elif or else statement as it is more readable and cleanner syntax.

# day_of_the_week = 2
# if day_of_the_week == 1:
#     print("Monday")
# elif day_of_the_week == 2:
#     print("Tuesday")
# elif day_of_the_week == 3:
#     print("Wednesday")
# else:
#     print("invalid")

#! The IF and Elif, Statement above is hard to read. We can use match case statement for more readable and cleanner. 

# def exam():
#     day_of_the_week = 3
#     match day_of_the_week:
#         case 1:
#             print("Monday")
#         case 2:
#             print("Tuesday")
#         case 3:
#             print("Wednesday")
#         case _:                 # * case _: is the else statement.
#             print("invalid")


#! This case statement execute code if the value match with the case.

#! case is also use with | (or) operator.

# card_status = int(input("Enter card status: "))
# match card_status:
#     case 200 | 300 | 400:
#         print("Active")
#     case 500 | 600 | 700:
#         print("Inactive")
#     case _: 
#         print("Unknow")
    
weekend_checker = "March"
match weekend_checker:
    case "Saturday" | "Sunday":
        print("Weekend")
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print("Not weekend")
    case _:
        print("Invalid")

#! Write a program, takes two numbers and operators (+,-,*,/)

def calculator():
    print("This is a calculator Program")
    z = (input("Choose the operators (+,-,*,/): "))
    x = int(input("Choose First Number: "))
    y = int(input("Choose Second Number: "))

    match z:
        case '+':
            result = x + y
            print(result)
        case '-':
            result = x - y
            print(result)
        case '*':
            result = x * y
            print(result)
        case '/':
            result = x / y
            print(result)