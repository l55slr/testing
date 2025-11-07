print("Salar Bank")
pin = int(input("plz enter ur pin: "))

while pin != 1234:
    pin = int(input("ur pin is not right. plz enter ur correct pin: "))
if pin == 1234:
    print("Your pin is correct")

#<---- with the and operator ---->
guess = 0
tries = 0
while guess != 6 and tries < 5:
  guess = int(input("guess the number in my mind: "))
  tries += 1
if guess != 6:
    print("Your got the limit")
else:
    print("You are smart")