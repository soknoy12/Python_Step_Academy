import random
guess=int(input("guess the number betwen 1-100:"))
rightNum=random.randint(1,100)
count = 1
while guess != rightNum:
    if guess > rightNum :
        print("your number is to high")
    else:
        print("your number is to low")
    guess=int(input("guess the number betwen 1-100:"))
    count+=1
print(f"correct you have tried {count} times")
