unit = input("What is the unit? C/F: ")
temp = float(input("What is the temperature? "))

if unit == "C":
    temp = round((temp * 9) / 5 + 32, 1)
    print(f"The temperature in F: {temp}")

elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature in C: {temp}")

else:
    print("Please enter a valid unit")
