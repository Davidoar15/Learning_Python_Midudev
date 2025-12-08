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
