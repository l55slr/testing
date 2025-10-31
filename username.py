# result = len (name)
# result = name. find("0")
# result = name.rfind("q")
# name = name.capitalize()
# name = name. upper ()
# name = name. lower)
# result = name. isdigit()
# result = name. isalpha()
# result = phone_number. count("-")
#phone_number = phone_number. replace("-", " ")

username = input("please enter your username: ")

if len(username) > 12:
    print("the username cannot be longer than 12 characters")
elif not username.find(" ") == -1:
    print("the username cannot have spaece ")
elif not username.isdigit() == False:
    print("the username cannot have number ")
else:
    print(f"welcome {username}")

