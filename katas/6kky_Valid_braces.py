""" Write a function that takes a string of braces, and determines if the order of the braces is valid. It should return true if the string is valid, and false if it's invalid.

This Kata is similar to the Valid Parentheses Kata, but introduces new characters: brackets [], and curly braces {}. Thanks to @arnedag for the idea!

All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: ()[]{}.
What is considered Valid?

A string of braces is considered valid if all braces are matched with the correct brace.
Examples

"(){}[]"   =>  True
"([{}])"   =>  True
"(}"       =>  False
"[(])"     =>  False
"[({})](]" =>  False

 """

def validBraces(string):
    c_br = 0
    q_br = 0
    r_br = 0

    #arr = [x for x in string]
    for x in range(1, len(string)):
        if string[x] == ']' and (string[x-1] == '{' or string[x-1] == '('):
            return False
        elif string[x] == '}' and (string[x-1] == '(' or string[x-1] == '['):
            return False
        elif string[x] == ')' and (string[x-1] == '{' or string[x-1] == '['):
            return False       
    
    for x in string:        
        if x == '{':
            c_br += 1
        elif x == '}':
            c_br -= 1
        elif x == '[':
            q_br += 1   
        elif x == ']':
            q_br -= 1   
        elif x == '(':
            r_br += 1
        elif x == ')':
            r_br -= 1
        if c_br < 0 or q_br < 0 or r_br < 0:
            return False
    return not c_br and not q_br and not r_br

print(validBraces("()"))
#True
print(validBraces("[(])"))
#False