# 1. import regular expressions module
import re

# 2. create a pattern (text string that describes what you want to find)
pattern = "Hello"

# 3. the text where you want to search
text = "Hello world"

# 4. use the "re" search function
result = re.search(pattern, text)
                                       # or None 
print(type(result), result, sep=" | ") # <class 're.Match'> | <re.Match object; span=(0, 5), match='Hello'>

if result: print("The pattern has been found in the text")
else: print("The pattern was NOT found in the text")

# returns the string that matches the pattern 
print(result.group()) # type: ignore | Hello

# returns the initial position of the match 
print(result.start()) # type: ignore | 0

# return the final position of the match
print(result.end()) # type: ignore | 5

# return a list with all matches
text2 = "I like Python. Python is the best. And Python is not difficult, what awesome is Python!"
pattern2 = "Python"
matches = re.findall(pattern2, text2)
print(matches, len(matches), sep=" | ") # ['Python', 'Python', 'Python', 'Python'] | 4

# return an iterator containing all the search results
matches2 = re.finditer(pattern2, text2)
for match in matches2: print(match.group(), match.start(), match.end(), sep=" | ")
# Python | 7  | 13
# Python | 15 | 21
# Python | 39 | 45
# Python | 80 | 86

# ? Modifiers. Options that can be added to a pattern to change its behavior
# * re.IGNORECASE
text3 = "I like python. Python is the best. And python is not difficult, what awesome is PYTHON!"
pattern3 = "python"
found_py = re.search(pattern3, text3, re.IGNORECASE)
pys = re.findall(pattern3, text3, re.IGNORECASE)
if found_py: 
    print(f"The pattern has been found in the text in the position { found_py.start() } and ends in the position { found_py.end() }")
    print(pys)

    # The pattern has been found in the text in the position 7 and ends in the position 13
    # ['python', 'Python', 'python', 'PYTHON']
else: 
    print("The pattern was NOT found in the text")

# replaces all pattern matches in text
text4 = "Hello World! and hello again."
pattern4 = "Hello"
replacement = "Goodbye"
                                               # count. Default 0
new_text = re.sub(pattern4, replacement, text4,      0           , re.IGNORECASE)
print(new_text) # Goodbye World! and Goodbye again.
