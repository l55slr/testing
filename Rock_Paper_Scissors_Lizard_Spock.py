import random
print("====================")
print("Rock Paper Scissors")
print("====================")
print("1) ✊ Rock")
print("2) ✋ Paper")
print("3) ✌️ Scissors")
print("4) 🦎 Lizard")
print("5) 🖖 Spock")
player = int(input("Enter your choice: "))

if player == 1:
    print("You chose: ✊ Rock")
elif player == 2:
    print("You chose: ✋ Paper")
elif player == 3:
    print("You chose: ✌️ Scissors")
elif player == 4:
    print("You chose: 🦎️ Lizard")
elif player == 5:
    print("You chose: 🖖️ Spock")
else:
    print("the input is invalid")

computer = random.randint(1,5)
if computer == 1:
    print("CPU chose:  ✊ Rock")
elif computer == 2:
    print("CPU chose:  ✋ Paper")
elif computer == 3:
    print("CPU chose: ✌️  Scissors")
elif computer == 4:
    print("CPU chose: 🦎  Lizard")
else:
    print("CPU chose: 🖖  Spock")


if player == computer:
    print("it's a tie!")
elif (player == 1 and computer == 3) or \
    (player == 2 and computer == 1) or \
    (player == 3 and computer == 2) or \
    (player == 3 and computer == 4) or \
    (player == 4 and computer == 5) or \
    (player == 5 and computer == 3) or \
    (player == 4 and computer == 2) or \
    (player == 2 and computer == 5) or \
    (player == 5 and computer == 1):
        print ("You win! 🎉")
else:
    print("CPU wins! 💻")