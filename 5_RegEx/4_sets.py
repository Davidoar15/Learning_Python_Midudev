import re 

# ! [:] Matches any character within the brackets
# username = "fol.$gor_03"
# pattern = r"[\w._%+-]+"
# match = re.search(pattern, username)
# if match: print("The username is valid: ", match.group()) # The username is valid:  fol.
# else: print("The username is not valid")

username = "fol.$gor_03"
pattern = r"^[\w._%+-]+$"
match = re.search(pattern, username)
if match: print("The username is valid: ", match.group()) 
else: print("The username is not valid") # The username is not valid

# ? RegEx to find man, fan and ban, but ignore the rest
text = "man fan ran kan, ban, san"
pattern_ex = r"[mfb]an" 
matches = re.findall(pattern_ex, text)
print(matches) # ['man', 'fan', 'ban']


# ! [^] Matches any character that is not inside the brackets
string = "Hello World"
ptrn = r"[^aeiou]"
matches = re.findall(ptrn, string)
print(matches) # ['H', 'l', 'l', ' ', 'W', 'r', 'l', 'd']
