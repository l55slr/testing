print("Salar Bank")
pin = int(input("plz enter ur pin: "))

while pin != 1234:
    pin = int(input("ur pin is not right. plz enter ur correct pin: "))
if pin == 1234:
    print("Your pin is correct")