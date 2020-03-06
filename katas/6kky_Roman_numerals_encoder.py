""" Create a function taking a positive integer as its parameter and returning a string containing the Roman Numeral representation of that integer.

Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.

Example:

solution(1000) # should return 'M'

Help:

Symbol    Value
I          1
V          5
X          10
L          50
C          100
D          500
M          1,000

Remember that there can't be more than 3 identical symbols in a row. """

def solution(n):    
    d = {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'}
    res = ''

    s = str(n)    
    for i in range(len(s)):           
        x = int(s[i])
        k = 10**(len(s) - i - 1)  
        
        if x <= 3:
            res += d[k] * x
        elif x == 4:
            res += d[k] + d[k*5]
        elif 5 <= x <= 8:
            res += d[k*5] + d[k] * (x - 5)
        else:
            res += d[k] + d[k*10]

    return res
            
 # print(solution(1),'I', "solution(1),'I'")
#print(solution(4))
# 'IV'
# print(solution(6),'VI', "solution(6),'VI'")
#print(solution(14))
# 'XIV"
# print(solution(21),'XXI', "solution(21),'XXI'")
# print(solution(89),'LXXXIX', "solution(89),'LXXXIX'")
print(solution(91))
# 'XCI'
# print(solution(984),'CMLXXXIV', "solution(984),'CMLXXXIV'")
# print(solution(1000), 'M', 'solution(1000), M')
# print(solution(1889),'MDCCCLXXXIX', "solution(1889),'MDCCCLXXXIX'")
# print(solution(1989),'MCMLXXXIX', "solution(1989),'MCMLXXXIX'")