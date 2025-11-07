print("to ride the the cyclone u should be 137 cm and have 10 credits")
height = int(input("How tall are you? "))
credits = int(input("How much do you have? "))
if height >= 137 and credits >=10:
  print("Enjoy the ride!")
elif height < 137 and credits >=10:
  print("You are not tall enough to ride")
elif height > 137 and credits <10:
  print("You don't have enough credits")
else:
  print("You ave not met either requirement.")