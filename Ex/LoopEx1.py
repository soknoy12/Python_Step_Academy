gryffindor = 0
hufflepuff = 0
ravenclaw = 0
slytherin = 0
print("Q1: Do you like Dawn or Dusk?\n1, Dawn.\n2, Dusk")
q1 = int(input("Pick a number: "))
if q1 == 1:
    gryffindor += 1
    ravenclaw += 1
elif q1 == 2:
    hufflepuff += 1
    slytherin += 1
else:
    print("Wrong input")
print("Q2: When I’m dead, I want people to remember me as:\n1, The Good\n2, The Great\n3, The Wise\n4, The Bold")
q2 = int(input("Pick a number: "))
if q2 == 1:
    hufflepuff += 2
elif q2 == 2:
    slytherin += 2
elif q2 == 3:
    ravenclaw += 2
elif q2 == 4:
    gryffindor += 2
else:
    print("Wrong input")
print("Q3: Which kind of instrument most pleases your ear?\n1, The violin\n2, The trumpet\n3, The piano\n4, The drum")
q3 = int(input("Pick a number: "))
if q3 == 1:
    slytherin += 4
elif q3 == 2:
    hufflepuff += 4
elif q3 == 3:
    ravenclaw += 4
elif q3 == 4:
    gryffindor += 4
else:
    print("Wrong input")
if gryffindor >= hufflepuff and gryffindor >= ravenclaw and gryffindor >= slytherin:
    print("You belong in Gryffindor")
elif hufflepuff >= gryffindor and hufflepuff >= ravenclaw and hufflepuff >= slytherin:
    print("You belong in Hufflepuff")
elif ravenclaw >= gryffindor and ravenclaw >= hufflepuff and ravenclaw >= slytherin:
    print("You belong in Ravenclaw")
elif slytherin >= gryffindor and slytherin >= hufflepuff and slytherin >= ravenclaw:
    print("You belong in Slytherin")
else:
    print("You have a tie between two or more houses, please retake the quiz")
