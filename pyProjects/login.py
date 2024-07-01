user1 = {"name":"", "pass":""}
print("Please Sign up first.... ")
user1["name"] = input("Enter Your Name: ")
user1["pass"] = input("Create a Password: ")
print("Login to continue.... ")
x = input("Name: ")
if x == user1["name"]:
    y = input("Password: ")
    if y == user1["pass"]:
        print("Congratulations You are a gay!")
    else:
        print("Do you know? /nYou are a gay!")
else:
    print("You are still a gay!")