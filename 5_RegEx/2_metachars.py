import re

# ! 1. (.)
# * Match any character except a newline
# text = "Hello world, hEllo again, h3llo again x2."
# pattern = "H.llo"
# found = re.findall(pattern, text, re.IGNORECASE)

# if found: print(found) # ['Hello', 'hEllo', 'h3llo']
# else: print("The pattern was NOT found in the text")

# ? Better for RegEx: pattern = r"..."
text = "Hello world, hEllo again, h3llo again x2."
pattern = r"H.llo"
found = re.findall(pattern, text, re.IGNORECASE)

if found: print(found) # ['Hello', 'hEllo', 'h3llo']
else: print("The pattern was NOT found in the text")


# ! r"\ ... " (\) To nullify the special meaning of a symbol
text2 = "Hello. I'm hungry. And I must to study."
pattern2 = r"\."
found2 = re.findall(pattern2, text2)

if found2: print(found2) # ['.', '.', '.']
else: print("The pattern was NOT found in the text")


# ! (\d) Matches with any digit (0 - 9). Only one
text3 = "Number phone is 123456765432"
found3 = re.findall(r"\d", text3)
found3_alt = re.findall(r"\d{12}", text3)
print(found3) # ['1', '2', '3', '4', '5', '6', '7', '6', '5', '4', '3', '2']
print(found3_alt) # ['123456765432']


# ! (\w) Matches with any alphanumeric character (a-z, A-Z, 0-9, ...)
text4 = "@folagor_03"
pattern4 = r"\w"
found4 = re.findall(pattern4, text4)
print(found4) # ['f', 'o', 'l', 'a', 'g', 'o', 'r', '_', '0', '3']


# ! (\s) Matches with any whitespace (spacing, tabulation, line break)
text5 = "Hello world\nHow are you?\t"
pattern5 = r"\s"
matches = re.findall(pattern5, text5)
print(matches) # [' ', '\n', ' ', ' ', '\t']


# ! (^) Matches with the beginning of a string
text6 = "423_name"
pattern6 = r"^\w" # start with alphanumeric character
valid = re.search(pattern6, text6)
if valid: print("The username is valid!") 
else: print("The username is not valid")

phone = "+54 1124016394"
pattern_phone = r"^\+\d{1,3} "
valid_phone = re.search(pattern_phone, phone)
if valid_phone: print("The number phone is valid!") 
else: print("The number phone is not valid")


# ! ($) Matches with the end of a string
text7 = "Hello world"
pattern7 = r"world$"
valid_text = re.search(pattern7, text7)
if valid_text: print("The string is valid!") 
else: print("The string is not valid")


# ! (\b) Matches with the beginning or end of a word
text8 = "casa casado casada Casa"
pattern8 = r"\bcasa\b"
found8 = re.findall(pattern8, text8, re.IGNORECASE)
print(found8) # ['casa', 'Casa']


# ! (|) Match with an option or other
fruits = "banana, apple, pear, peach, tomato, apple, peer, TOMATOES"
pattern_fruits = r"apple|tomato|p..r|\b\w{6}\b"
matches = re.findall(pattern_fruits, fruits)
print(matches) # ['banana', 'apple', 'pear', 'tomato', 'apple', 'peer']