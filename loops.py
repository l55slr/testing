for i in range (10, 0, -1):
  print(i)
print("Happy New Year! 🥳")

print("<============================>")
import random
die1 = random.randint(1, 6)
die2 = random.randint(1, 6)
total = die1 + die2

while total != 2:
    print("Nope")
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
else:
    print("Snake eyes!")