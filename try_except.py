# try: ...except:
num = input("Enter your number: ")

try:
    num = int(num)
    print("Your number is ", num)
except:
    print(num.upper(),"is not a number.") 
    # .upper() to make letter capitalize for num value
    print(num,"is not a number.")


