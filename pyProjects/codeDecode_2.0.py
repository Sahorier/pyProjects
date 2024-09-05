import os
import random
def clear():
    # Check if the system is Windows      (clear function Taken from pieces)
    if os.name == 'nt':
        os.system('cls')
    # For Unix-based systems
    else:
        os.system('clear')

def echange(target):
    target = target.replace("a", "1")
    target = target.replace("b", "2")
    target = target.replace("c", "3")
    target = target.replace("d", "4")
    target = target.replace("e", "5")
    target = target.replace("f", "6")
    target = target.replace("g", "7")
    target = target.replace("h", "8")
    target = target.replace("i", "9")
    # target = target.replace("j", "0")
    target = target.replace("k", "!")
    target = target.replace("l", "@")
    target = target.replace("m", "#")
    target = target.replace("n", "$")
    target = target.replace("o", "%")
    target = target.replace("p", "&")
    target = target.replace("q", "?")
    target = target.replace("r", "~")
    # target = target.replace("s", "a")
    # target = target.replace("t", "b")
    # target = target.replace("u", "c")
    # target = target.replace("v", "d")
    # target = target.replace("w", "e")
    # target = target.replace("x", "f")
    # target = target.replace("y", "g")
    # target = target.replace("z", "h")
    # target = target.replace(" ", "s")
    return target

def dchange(target):
    target = target.replace("1", "a")
    target = target.replace("2", "b")
    target = target.replace("3", "c")
    target = target.replace("4", "d")
    target = target.replace("5", "e")
    target = target.replace("6", "f")
    target = target.replace("7", "g")
    target = target.replace("8", "h")
    target = target.replace("9", "i")
    # target = target.replace("0", "j")
    target = target.replace("!", "k")
    target = target.replace("@", "l")
    target = target.replace("#", "m")
    target = target.replace("$", "n")
    target = target.replace("%", "o")
    target = target.replace("&", "p")
    target = target.replace("?", "q")
    target = target.replace("~", "r")
    # target = target.replace("a", "s")
    # target = target.replace("b", "t")
    # target = target.replace("c", "u")
    # target = target.replace("d", "v")
    # target = target.replace("e", "w")
    # target = target.replace("f", "x")
    # target = target.replace("g", "y")
    # target = target.replace("h", "z")
    return target
if __name__ == "__main__":
    randomword = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    print("Welcome to RH Encode/Decoder!")
    print("Are you want to Encode or decode?")
    choice = input("Enter 1 to encode or 2 to decode \n> ")
    clear()
    print("M@de By RH")
    text = input("   Enter the text\n>> ")
    textlist = text.split(" ")
    codelist = []
    decodedlist = []
    codecode = ""
    decode = ""
    if choice == "1":
        for i in textlist:
            if len(i) < 3:
                i = i[::-1]
                i = echange(i)
                i = i.swapcase()
                codelist.append(i)
                
            else:
                i = i[1:] + i[:1]
                i = random.choice(randomword) + random.choice(randomword) + random.choice(randomword) + i + random.choice(randomword) + random.choice(randomword) + random.choice(randomword) 
                i = echange(i)
                i = i.swapcase()
                codelist.append(i)

    elif choice == "2":
        text = text.swapcase()
        decodelist = text.split("0")
        for b in decodelist:
            if len(b) < 3:
                b = b[::-1]
                b = dchange(b)
                decodedlist.append(b)
            else:
                b = b[-4:-3] + b[3:-4]
                b = dchange(b)
                decodedlist.append(b)

    codecode = "0".join(codelist)
    print(codecode)

    decode = " ".join(decodedlist)
    print(decode.capitalize())


