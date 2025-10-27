#The "or" logical, for this logical one condition must be true
x = 5
y = 10
if x > 100 or y < 10 :
    print("the condition is valid")
else:
    print("the condition is invalid")


temp = 20
raining = False
if temp < 30 or raining:
    print("we can go")
else:
    print("we can't go")

#the "and" logical, both condition must be true
age = 18
has_id = False
vip = True

if (age >= 18 and has_id) or vip:
    print("we can go")
else:
    print("we can not go")






