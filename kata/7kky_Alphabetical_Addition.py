def add_letters(*letters):
    return chr(96 + (sum(ord(l) - 96 for l in letters) % 26 or 26))

#print(add_letters('a', 'b', 'c'))
# = 'f' 
print(add_letters('z'))
# z