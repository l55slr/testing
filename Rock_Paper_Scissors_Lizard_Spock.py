import random
print("====================")
print("Rock Paper Scissors")
print("====================")
print("1) ✊ Rock")
print("2) ✋ Paper")
print("3) ✌️ Scissors")
player = int(input("Enter your choice: "))

if player == 1:
    print("You chose: ✊ Rock")
elif player == 2:
    print("You chose: ✋ Paper")
elif player == 3:
    print("You chose: ✌️ Scissors")
else:
    print("the input is invalid")

computer = random.randint(1,3)
if computer == 1:
    print("CPU chose:    Rock")
elif computer == 2:
    print("CPU chose:    Paper")
else:
    print("CPU chose: ✌️ Scissors")

if player == computer:
    print("it's a tie!")
elif (player == 1 and computer == 3) or \
    (player == 2 and computer == 1) or\
    (player == 3 and computer == 2):
    print ("you win")
else:
    print("cpu win")