names = {"hi",2,3,4,"hello",6,"bye",8,9,10}#names = {"hi",2,3,4,"hello",6,"bye",8,9,10}#names = { input("Participent1: "),input("participent2: "), input("participent3: "), input("participent4: "), input("Participent5: "), input("Participent6: "), input("Participent7: "), input("Participent8: "), input("Participent9: "), input("Participent10: ")}
for x in range(len(names)):
    if x == 7:
        break
    names = list(names)
    print(names[x])
    print("Press enter to continue")
    for chance in range(1,4):
        password = input("")
        if password == "":
            names = set(names)
            for y in range(len(names)):
                if y == 4:
                    break
                names = list(names)
                print(names[y])
                print("Press enter to continue")
                for chance1 in range(1,4):
                    password1 = input("")
                    if password1 == "":
                        names = set(names)
                        for z in range(len(names)):
                            if z == 2:
                                names = list(names)
                                print(names[z])
                        break
                    h = f"Press enter to continue {chance}/3"
                    print(h)
                    if h == "Press enter to continue 3/3":
                        print("    404 ERROR")
            break
        h1 = f"Press enter to continue {chance}/3"
        print(h)
        if h == "Press enter to continue 3/3":
            print("   404 ERROR")
    
    