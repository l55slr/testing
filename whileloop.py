name = input("what is your name?")
while name == "":
    print("enter ur name")
    name = input("what is your name?")
print(f"hello {name}")



age = input("what is your age? ")
while age == "":
    age = input("what is your age? ")
age = int(age)
if age >= 18:
    print(f"{age} is what we looking for.")
else:
    print(f"{age}your age is not what we looking for.")
