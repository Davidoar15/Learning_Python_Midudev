import re 

# ! (*) Can appear 0 or more times
string = "aaaba"
pattern = r"a*"
matches = re.findall(pattern, string)
print(matches) # ['aaa', '', 'a', '']


# ! (+) Can appear ONE or more times
string2 = "dddd aaa ccc a bb aa casa"
pattern2 = r"a+"
matches2 = re.findall(pattern2, string2)
print(matches2) # ['aaa', 'a', 'aa', 'a', 'a']


# ! (?) Can appear 0 or ONE time
string3 = "aaabacb"
pattern3 = r"a?b"
matches3 = re.findall(pattern3, string3)
print(matches3) # ['ab', 'b']


# ! {n} Appears exactly n times
str4 = "aaaaaa aa aaaa"
ptrn4 = r"a{3}"
matches4 = re.findall(ptrn4, str4)
print(matches4) # ['aaa', 'aaa', 'aaa']

# ? {n, m}
str4_alt = "u uu uuu uuuu u"
ptrn4_alt = r"u{2,3}"
matches4_alt = re.findall(ptrn4_alt, str4_alt)
print(matches4_alt) # ['uu', 'uuu', 'uuu']
