languages= ["Swift", "Python","Go"]
character = "Python"

for lang in languages:
    print(lang)
for _ in character:
    print(_)

#EX 1: 
# import time
# for idx in range(0, len(languages)):
#     name = input("Enter your name: \n")
#     print("NO.", idx+1, "=", languages[idx])
#     time.sleep(3)


#EX 2:
multiplicaton = int(input("Enter multiplication of : "))
for idc in range(0, 11):
    result = multiplicaton * idc
    print(f"{idc} x {multiplicaton} = {result}")
   


