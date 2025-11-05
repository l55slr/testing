gryffindor = 0
hufflepuff = 0
ravenclaw = 0
slytherin = 0
#Q1
print("Q1) Do you like Dawn or Dusk? ")
print("1)  Dawn")
print("2)  Dusk")
answer = int(input("Enter your answer (1-2) "))

if answer == 1:
    gryffindor = gryffindor +1
    ravenclaw = ravenclaw +1
elif answer == 2:
    hufflepuff = hufflepuff +1
    slytherin = slytherin +1
else:
    print("Wrong input")

#Q2
print("Q2) When I’m dead, I want people to remember me as: ")
print("1)  The Good")
print("2)  The Great")
print("3)  The Wise")
print("4)  The Bold")
answer = int(input("Enter your answer (1-4) "))

if answer == 1:
    hufflepuff = hufflepuff +2
elif answer == 2:
    slytherin = slytherin +2
elif answer == 3:
    ravenclaw = ravenclaw +2
elif answer == 4:
    gryffindor = gryffindor +2
else:
    print("Wrong input.")

#Q3
print("q3) Which kind of instrument most pleases your ear? ")
print("1)  The violin")
print("2)  The trumpet")
print("3)  The piano")
print("4)  The drum")
answer = int(input("Enter your answer (1-4)"))

if answer == 1:
    hufflepuff = hufflepuff +4
elif answer == 2:
    slytherin = slytherin +4
elif answer == 3:
    ravenclaw = ravenclaw +4
elif answer == 4:
    gryffindor = gryffindor +4
else:
    print("Wrong input.")


