""" Count the number of Duplicates

Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.
Example

"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice
 """
def duplicate_count(text):    
    t = text.lower()
    c = 0
    for i in set(t):
        if t.count(i) > 1:
            c += 1
    return c  

print(duplicate_count('Indivisibilities'))
# 2
#test.assert_equals(duplicate_count("abcde"), 0)
#test.assert_equals(duplicate_count("abcdea"), 1)
#test.assert_equals(duplicate_count("indivisibility"), 1)