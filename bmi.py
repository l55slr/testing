mass = float(input("put ur mass in KG"))
height = float(input("put ur height meters "))
bmi = mass / (height **2)
print(f"Your BMI is {round(bmi,2)}")

if bmi < 18.5:
    print("you are underweight")
elif bmi < 25:
    print("you are normal")
elif bmi < 30:
    print("you are overweight")
else :
    print("you are obese")



