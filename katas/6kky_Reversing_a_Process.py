""" Suppose we know the process (A) by which a string s has been coded to a string r.

The aim of the kata is to decode r to get back the original string s.
Explanation of the known process (A):

    data: a string s composed of lowercase letters from a to z and a positive integer num

    we know there is a correspondence between abcde...uvwxyzand 0, 1, 2 ..., 23, 24, 25 : 0 <-> a, 1 <-> b ...

    if c is a character of s whose corresponding number is x, apply to x the function f: x-> f(x) = num * x % 26 then find ch the corresponding character of f(x)

    Accumulate all these ch in a string r.

    concatenate num and r and return the result.
    Example:

    code("mer", 6015) -> "6015ekx"
    m <-> 12, 12 * 6015 % 26 == 4, 4 <-> e
    e <-> 4, 4 * 6015 % 26 == 10, 10 <-> k
    r <-> 17, 17 * 6015 % 26 == 23, 23 <-> x
    We get "ekx" hence "6015ekx"

Task

A string s has been coded to a string r by the above process (A). Write a function r -> decode(r) to get back s whenever it is possible.

Indeed it can happen that the decoding is impossible when positive integer num has not been correctly chosen. In that case return "Impossible to decode".
Example:

decode("6015ekx") -> "mer"
decode("5057aan") -> "Impossible to decode"

Note

Please could you ask before translating : some translations are already written.
 """
import re
def decode(r):
    a = int(''.join(re.findall('[0-9]', r)))   
    s = re.findall('[a-z]', r)     
    mod = 26
    res = ''
   
    a = a % mod
    for ch in s:
        new_ch = ''
        for x in range(mod):
            if x * a % mod == ord(ch) % 97:                
                if new_ch:
                    return 'Impossible to decode!'
                new_ch += chr(x % mod + 97)                
        else:
            res += new_ch
    return res
    

print(decode("1273409kuqhkoynvvknsdwljantzkpnmfgf"))
#"uogbucwnddunktsjfanzlurnyxmx"
print(decode("761328qockcouoqmoayqwmkkic"))
#"Impossible to decode"
print(decode("5057abcdefghijk"))
#"Impossible to decode"
#testing_decode("1544749cdcizljymhdmvvypyjamowl", "mfmwhbpoudfujjozopaugcb")
#testing_decode("1122305vvkhrrcsyfkvejxjfvafzwpsdqgp", "rrsxppowmjsrclfljrajtybwviqb")