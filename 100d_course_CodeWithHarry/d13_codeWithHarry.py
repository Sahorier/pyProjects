#  String Methods in Python.
#  Those who returns bool type data are mostly used for if else function.
st1 = "HelLo Moontonnn"
print(st1)
print(st1.strip())  # Removes space from start and end.
print(st1.upper())  # Makes all character uppercase.
print(st1.lower())  # Makes all character lowercase.
print(st1.rstrip("n"))  # Removes selected character from the end.
print(st1.split("n"))  # Splits strings from the selected character and arrange them in a list.
print(st1.replace("n", "m"))  # Replaces selected word/character with new one.
print(st1.capitalize())  # Makes first character of the first word capital.
print(st1.center(60))  # Makes the length of the Word or Paragraph to the desired length by adding spaces in the start.
print(len(st1.center(60)))
print(st1.count("n"))  # Counts the length.
print(st1.endswith("n"))  # verifies if the word ends with n.
print(st1.endswith("m"))
print(type(st1.endswith("n")))
print(st1.find("n"))  # Finds the character.
print(st1.find("i"))  # If it can't find, returns -1.
print(st1.index("n"))  # same as find.
# print(st1.index("i"))  # If can't find throws an error.
print(st1.isalnum())  # Verifies if the word is alphanumeric or not, (A-Z, a-z, 0-9) [ Spaces can also return false ]
x = "skjfls49"
print(x.isalnum())
print(x.isalpha())  # Verifies if the word is alphabet (Numbers are also not allowed)
print(x.islower())  # Verifies if the word is in lowercase or not.
print(x.isprintable())  # Verifies if the word is printable or not ( \ is not printable in a string )
y = "hi, my name is\nNafiz"  # Here \n doesn't print, it causes a newline.
print(y.isprintable())
z = "   "
print(z.isspace())  # Verifies if it is a space or not.
a = "Hi my name is Nafiz"
print(a.istitle())  # Verifies if the sentence is a title or not. ( a title contains an uppercase character in every
# words in the sentence )
#  isupper is same as islower
print(a.startswith("H"))  # Verifies if the paragraph or word starts with the selected character or not.
print(a.swapcase())  # Makes the upper one lower and the lower one upper.
print(a.title())  # Converts a paragraph or sentence to title.
