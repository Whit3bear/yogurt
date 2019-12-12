""" If we alternate the vowels and consonants in the string "have", we get the following list, arranged alphabetically: ['ahev', 'aveh', 'ehav', 'evah', 'vahe', 'veha']. These are the only possibilities in which vowels and consonants are alternated. The first element, ahev, is alphabetically lowest.

Given a string:

    alternate the vowels and consonants and return the lexicographically lowest element in the list
    If any two or more vowels or consonants must follow each other, return "failed"
    if the number of vowels and consonants are equal, the first letter of the result must be a vowel.

Examples:

solve("codewars") = "failed". However you alternate vowels and consonants, two consonants must follow each other
solve("oruder") = "edorur"
solve("orudere") = "ederoru". This is the only option that allows you to alternate vowels & consonants.

In C, return an allocated string even if the response is "failed".

Vowels will be any of "aeiou". Input will be a lowercase string, no spaces. See test cases for more examples.

Good luck!

If you like this Kata, please try:

Consonant value

Alternate capitalization
 """
import itertools

def solve(s):
    vowels = 'aeiou'
    s_vow = sorted([x for x in s if x in vowels])
    s_cons = sorted([x for x in s if x not in vowels])    

    if abs(len(s_cons) - len(s_vow)) > 1:
        return 'failed'
    
    l = [x[::-1] if len(s_cons) > len(s_vow) else x for x in itertools.zip_longest(s_vow, s_cons, fillvalue='')]    
    res = ''

    for item in l:
        res += '{}{}'.format(*item)      

    return res

print(solve("java"))
# 'ajav'
print(solve("oruder"))
#'edorur'
print(solve("zodiac"))
#'acidoz'