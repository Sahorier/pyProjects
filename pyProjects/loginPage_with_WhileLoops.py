user1= {"name":"","pass":""}
print("Please sign up first.")
user1["name"] = input("Enter Your Name: ")
user1["pass"] = input("Create a password: ")
print("login to continue...")
n = input("Name: ")

while (user1["name"]!= n):
    print("Incurrect username! Try again.")
    n = input("Name: ")
else:
    p = input("Password: ")
    while (user1["pass"] != p):
        print("Incurrect Password! Try again.")
        p = input("Password: ")

print("You are logged in!")



